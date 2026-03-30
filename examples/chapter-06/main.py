from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


@dataclass(frozen=True)
class RetrievedChunk:
    document: Document
    score: int


DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "shared"
    / "datasets"
    / "chapter-06"
    / "course_materials.json"
)


def load_course_materials(dataset_path: Path = DATASET_PATH) -> list[Document]:
    payload = json.loads(dataset_path.read_text(encoding="utf-8"))
    return [
        Document(page_content=item["page_content"], metadata={"source": item["source"]})
        for item in payload
    ]


def split_documents(
    documents: Iterable[Document], chunk_size: int, chunk_overlap: int
) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
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


def score(question: str, chunk: Document) -> int:
    keywords = extract_signals(question)
    text = chunk.page_content.lower()
    return sum(1 for keyword in keywords if keyword in text)


def retrieve(question: str, chunks: list[Document], top_k: int) -> list[RetrievedChunk]:
    ranked = [RetrievedChunk(document=chunk, score=score(question, chunk)) for chunk in chunks]
    ranked.sort(key=lambda item: (item.score, len(item.document.page_content)), reverse=True)
    return [item for item in ranked[:top_k] if item.score > 0]


def compress_context(chunks: list[RetrievedChunk], max_chars: int = 240) -> str:
    text = "\n".join(
        f"[{item.document.metadata.get('source')}] {item.document.page_content}" for item in chunks
    )
    return text[:max_chars]


def answer(question: str, context: str, mode: str) -> str:
    if not context:
        return f"[{mode}] 资料不足，无法确定答案。"
    return (
        f"[{mode}] 基于检索片段可以判断：RAG 优化的关键是切分、检索、上下文和生成四层一起调。"
        f" 问题：{question}。证据摘要：{context}"
    )


def run_experiment(
    question: str, chunk_size: int, chunk_overlap: int, top_k: int, mode: str
) -> None:
    course_materials = load_course_materials()
    chunks = split_documents(course_materials, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    retrieved = retrieve(question, chunks, top_k=top_k)
    context = compress_context(retrieved)

    print("=" * 80)
    print(f"Mode: {mode}")
    print(f"Dataset: {DATASET_PATH.relative_to(Path(__file__).resolve().parents[2])}")
    print(f"Chunk size: {chunk_size}, overlap: {chunk_overlap}, top_k: {top_k}")
    print(f"Loaded documents: {len(course_materials)}")
    print(f"Chunks: {len(chunks)}")
    print("Retrieved:")
    for item in retrieved:
        print(
            f"- score={item.score} | "
            f"{item.document.metadata.get('source')}: {item.document.page_content}"
        )
    print(f"Compressed context: {context}")
    print(answer(question, context, mode))
    print()


def main() -> None:
    question = "第 6 章为什么强调不要只调模型？"
    run_experiment(question, chunk_size=50, chunk_overlap=0, top_k=2, mode="baseline")
    run_experiment(question, chunk_size=100, chunk_overlap=20, top_k=3, mode="optimized")


if __name__ == "__main__":
    main()
