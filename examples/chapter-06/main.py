from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pydantic import Field
from langchain_core.documents import Document
from langchain_core.language_models import FakeListChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
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


class KeywordRetriever(BaseRetriever):
    documents: list[Document] = Field(default_factory=list)
    top_k: int = 3

    def _get_relevant_documents(self, query: str) -> list[Document]:
        ranked = [RetrievedChunk(document=chunk, score=score(query, chunk)) for chunk in self.documents]
        ranked.sort(key=lambda item: (item.score, len(item.document.page_content)), reverse=True)
        return [item.document for item in ranked[: self.top_k] if item.score > 0]


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


def rewrite_query(question: str) -> str:
    return f"RAG 优化 切分 检索 上下文 生成 {question}"


def rerank_documents(question: str, documents: list[Document], limit: int = 3) -> list[Document]:
    ranked = sorted(documents, key=lambda document: score(question, document), reverse=True)
    return ranked[:limit]


def format_documents(documents: list[Document], max_chars: int = 260) -> str:
    if not documents:
        return ""
    joined = "\n\n".join(
        f"[{document.metadata.get('source', 'unknown')}] {document.page_content}"
        for document in documents
    )
    return joined[:max_chars]


def answer_with_framework(question: str, context: str, mode: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是课程学习助手。请只根据资料回答，并点明优化关注的是哪一层。"),
            ("human", "模式：{mode}\n问题：{question}\n\n资料：\n{context}"),
        ]
    )
    model = FakeListChatModel(
        responses=[
            f"[{mode}] 更接近真实 RAG 接口的版本会先取 retriever 结果，再做重排和上下文压缩，最后把证据送给模型回答。"
        ]
    )
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"mode": mode, "question": question, "context": context or "资料不足"})


def run_real_strategy(
    question: str, chunk_size: int, chunk_overlap: int, top_k: int, mode: str, rewrite: bool
) -> None:
    course_materials = load_course_materials()
    chunks = split_documents(course_materials, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    retriever = KeywordRetriever(documents=chunks, top_k=top_k)
    search_query = rewrite_query(question) if rewrite else question
    retrieved = retriever.invoke(search_query)
    reranked = rerank_documents(question, retrieved)
    context = format_documents(reranked)

    print("=" * 80)
    print(f"Real mode: {mode}")
    print(f"Search query: {search_query}")
    print(f"Chunk size: {chunk_size}, overlap: {chunk_overlap}, top_k: {top_k}")
    print("Retriever output:")
    for document in reranked:
        print(f"- {document.metadata.get('source')}: {document.page_content}")
    print(f"Compressed context: {context}")
    print(answer_with_framework(question, context, mode))
    print()


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
    run_real_strategy(question, chunk_size=60, chunk_overlap=0, top_k=2, mode="framework-baseline", rewrite=False)
    run_real_strategy(
        question,
        chunk_size=120,
        chunk_overlap=24,
        top_k=5,
        mode="framework-optimized",
        rewrite=True,
    )


if __name__ == "__main__":
    main()
