from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Iterable

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


@dataclass(frozen=True)
class RetrievedChunk:
    document: Document
    score: int


DATASET_PATH = Path(__file__).resolve().parents[2] / "shared" / "datasets" / "chapter-05" / "course_materials.json"


def load_course_materials(dataset_path: Path = DATASET_PATH) -> list[Document]:
    payload = json.loads(dataset_path.read_text(encoding="utf-8"))
    return [
        Document(page_content=item["page_content"], metadata={"source": item["source"]})
        for item in payload
    ]


def build_chunks(documents: Iterable[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=80, chunk_overlap=20)
    return splitter.split_documents(list(documents))


def extract_signals(text: str) -> set[str]:
    signals: set[str] = set()
    for token in re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]{2,}", text):
        if token.isascii():
            signals.add(token.lower())
            continue
        for index in range(len(token) - 1):
            signals.add(token[index : index + 2])
    return signals


def score_chunk(question: str, chunk: Document) -> int:
    question_terms = extract_signals(question)
    text = chunk.page_content.lower()
    return sum(1 for term in question_terms if term in text)


def retrieve(question: str, chunks: list[Document], top_k: int = 3) -> list[RetrievedChunk]:
    ranked = [RetrievedChunk(document=chunk, score=score_chunk(question, chunk)) for chunk in chunks]
    ranked.sort(key=lambda item: item.score, reverse=True)
    return [item for item in ranked[:top_k] if item.score > 0]


def synthesize_answer(question: str, retrieved: list[RetrievedChunk]) -> str:
    if not retrieved:
        return "资料不足，无法从课程文档中找到直接支持答案的内容。"

    lines = [
        "基于课程资料，给出的简要回答是：",
        "",
        f"问题：{question}",
        "",
        "参考片段：",
    ]
    for item in retrieved:
        source = item.document.metadata.get("source", "unknown")
        lines.append(f"- [{source}] {item.document.page_content}")
    lines.extend(
        [
            "",
            "结论：RAG 的价值在于先查资料，再回答，因此更适合课程站和私有知识问答。",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    course_materials = load_course_materials()
    chunks = build_chunks(course_materials)
    print(f"Dataset: {DATASET_PATH.relative_to(Path(__file__).resolve().parents[2])}")
    print(f"Loaded documents: {len(course_materials)}")
    print(f"Split chunks: {len(chunks)}")
    print()

    questions = [
        "为什么第 5 章要做 RAG，而不是直接问模型？",
        "第 6 章主要优化哪些部分？",
    ]

    for question in questions:
        retrieved = retrieve(question, chunks)
        print("=" * 80)
        print(f"Question: {question}")
        print("Retrieved chunks:")
        for item in retrieved:
            print(f"- score={item.score} | {item.document.metadata.get('source')}: {item.document.page_content}")
        print()
        print(synthesize_answer(question, retrieved))
        print()


if __name__ == "__main__":
    main()
