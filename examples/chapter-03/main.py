from __future__ import annotations

import json
import re
from dataclasses import dataclass

from pydantic import BaseModel, Field
from langchain_core.language_models import FakeListChatModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableLambda


@dataclass
class LearningPlan:
    topic: str
    audience: str


class StructuredLearningPlan(BaseModel):
    learning_goals: list[str] = Field(default_factory=list)
    core_concepts: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)


def extract_topic(prompt_text: str) -> LearningPlan:
    if hasattr(prompt_text, "to_string"):
        prompt_text = prompt_text.to_string()
    else:
        prompt_text = str(prompt_text)
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


def build_real_chain():
    parser = JsonOutputParser(pydantic_object=StructuredLearningPlan)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是 AI 学习助手，请严格输出 JSON。\n{format_instructions}"),
            ("human", "主题：{topic}\n读者：{audience}\n请给出结构化学习计划。"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())
    model = FakeListChatModel(
        responses=[
            json.dumps(
                {
                    "learning_goals": [
                        "理解 Prompt、Model、Parser 如何组合成可维护链路",
                        "知道什么时候从教学版升级到真实链式接口",
                    ],
                    "core_concepts": [
                        "ChatPromptTemplate",
                        "LCEL",
                        "JsonOutputParser",
                    ],
                    "next_steps": [
                        "把假模型替换成真实聊天模型",
                        "把结构化结果直接交给后续页面或服务层",
                    ],
                },
                ensure_ascii=False,
            )
        ]
    )
    return prompt | model | parser


def print_real_plan(plan: dict) -> None:
    print("learning_goals:")
    for item in plan["learning_goals"]:
        print(f"- {item}")
    print("core_concepts:")
    for item in plan["core_concepts"]:
        print(f"- {item}")
    print("next_steps:")
    for item in plan["next_steps"]:
        print(f"- {item}")


def main() -> None:
    input_payload = {
        "topic": "LangChain 核心抽象",
        "audience": "刚开始学习 LangChain 的初学者",
    }

    teaching_chain = build_chain()
    teaching_result = teaching_chain.invoke(input_payload)
    print("== 教学版 ==")
    print(teaching_result)
    print()

    real_chain = build_real_chain()
    real_result = real_chain.invoke(
        {
            "topic": "LangChain 核心抽象",
            "audience": "准备把教程示例升级成真实链式接口的读者",
        }
    )
    print("== 真实框架版 ==")
    print_real_plan(real_result)


if __name__ == "__main__":
    main()
