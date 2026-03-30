from __future__ import annotations

import re
from dataclasses import dataclass

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda


@dataclass
class LearningPlan:
    topic: str
    audience: str


def extract_topic(prompt_text: str) -> LearningPlan:
    topic_match = re.search(r"主题[:：]\s*(.+)", prompt_text)
    audience_match = re.search(r"读者[:：]\s*(.+)", prompt_text)
    topic = topic_match.group(1).strip() if topic_match else "LangChain"
    audience = audience_match.group(1).strip() if audience_match else "初学者"
    return LearningPlan(topic=topic, audience=audience)


def fake_model(prompt_text: str) -> str:
    plan = extract_topic(prompt_text)
    return (
        f"## 学习目标\n"
        f"- 理解 {plan.topic} 的核心作用\n"
        f"- 能把 {plan.topic} 拆成可维护的步骤\n"
        f"- 为后续 RAG、Agent 和 LangGraph 打基础\n\n"
        f"## 核心概念\n"
        f"- PromptTemplate\n"
        f"- Runnable / LCEL\n"
        f"- 输出解析\n"
        f"- 结构化思维\n\n"
        f"## 学习顺序\n"
        f"1. 先看整体流程\n"
        f"2. 再理解每个步骤的职责\n"
        f"3. 最后尝试替换模型实现\n\n"
        f"## 练习建议\n"
        f"- 把主题换成 `RAG 入门` 再运行一次\n"
        f"- 尝试修改 Prompt 里的约束，观察输出变化\n"
        f"- 给输出增加一个新的章节，例如 `常见坑`\n"
    )


def build_chain():
    prompt = PromptTemplate.from_template(
        "你是一个学习助手。\n读者：{audience}\n主题：{topic}\n请生成一份简洁的学习计划。"
    )
    model = RunnableLambda(fake_model)
    parser = StrOutputParser()
    return prompt | model | parser


def main() -> None:
    chain = build_chain()
    result = chain.invoke(
        {
            "topic": "LangChain 核心抽象",
            "audience": "刚开始学习 LangChain 的初学者",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
