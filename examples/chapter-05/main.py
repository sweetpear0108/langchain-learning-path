from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from langchain_core.documents import Document
from langchain_core.language_models import FakeListChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import Field


@dataclass(frozen=True)
class RetrievedChunk:
    document: Document
    score: int


DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "shared"
    / "datasets"
    / "chapter-05"
    / "course_materials.json"
)


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
    ranked = [
        RetrievedChunk(document=chunk, score=score_chunk(question, chunk)) for chunk in chunks
    ]
    ranked.sort(key=lambda item: item.score, reverse=True)
    return [item for item in ranked[:top_k] if item.score > 0]


class KeywordRetriever(BaseRetriever):
    documents: list[Document] = Field(default_factory=list)
    top_k: int = 3

    def _get_relevant_documents(self, query: str) -> list[Document]:
        ranked = [
            RetrievedChunk(document=document, score=score_chunk(query, document))
            for document in self.documents
        ]
        ranked.sort(key=lambda item: item.score, reverse=True)
        return [item.document for item in ranked[: self.top_k] if item.score > 0]


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


def format_documents(documents: list[Document]) -> str:
    if not documents:
        return "没有命中资料。"
    return "\n\n".join(
        f"[{document.metadata.get('source', 'unknown')}] {document.page_content}"
        for document in documents
    )


def build_real_rag_chain(chunks: list[Document]):
    retriever = KeywordRetriever(documents=chunks, top_k=3)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是课程学习助手。只能基于检索资料回答；资料不足时要明确说明。"),
            ("human", "问题：{question}\n\n资料：\n{context}"),
        ]
    )
    model = FakeListChatModel(
        responses=["RAG 更适合课程资料问答，因为链路会先检索课程内容，再依据命中的片段组织答案。"]
    )
    chain = (
        {
            "question": RunnablePassthrough(),
            "context": retriever | RunnableLambda(format_documents),
        }
        | prompt
        | model
        | StrOutputParser()
    )
    return retriever, chain


def run_teaching_demo(question: str, chunks: list[Document]) -> None:
    retrieved = retrieve(question, chunks)
    print("== 教学版 ==")
    print(f"Question: {question}")
    print("Retrieved chunks:")
    for item in retrieved:
        print(
            f"- score={item.score} | "
            f"{item.document.metadata.get('source')}: {item.document.page_content}"
        )
    print()
    print(synthesize_answer(question, retrieved))
    print()


def run_real_demo(question: str, chunks: list[Document]) -> None:
    retriever, chain = build_real_rag_chain(chunks)
    retrieved = retriever.invoke(question)
    print("== 真实框架版 ==")
    print(f"Question: {question}")
    print("Retriever output:")
    for document in retrieved:
        print(f"- {document.metadata.get('source')}: {document.page_content}")
    print()
    print(chain.invoke(question))


def main() -> None:
    course_materials = load_course_materials()
    chunks = build_chunks(course_materials)
    print(f"Dataset: {DATASET_PATH.relative_to(Path(__file__).resolve().parents[2])}")
    print(f"Loaded documents: {len(course_materials)}")
    print(f"Split chunks: {len(chunks)}")
    print()

    question = "为什么第 5 章要做 RAG，而不是直接问模型？"
    print("=" * 80)
    run_teaching_demo(question, chunks)
    run_real_demo(question, chunks)


if __name__ == "__main__":
    main()
