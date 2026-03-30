from __future__ import annotations

import re

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda


def parse_topic(prompt_text: str) -> str:
    match = re.search(r"主题[:：]\s*(.+)", prompt_text)
    return match.group(1).strip() if match else "LangChain 学习"


def toy_model(prompt_text: str) -> str:
    topic = parse_topic(prompt_text)
    if "Markdown 小标题" in prompt_text or "固定 4 个部分" in prompt_text:
        return (
            f"## 学习目标\n"
            f"- 让输出更稳定\n"
            f"- 让结果更适合网页展示\n\n"
            f"## 核心概念\n"
            f"- 任务层\n"
            f"- 约束层\n"
            f"- 格式层\n\n"
            f"## 学习顺序\n"
            f"1. 先定义任务\n"
            f"2. 再增加约束\n"
            f"3. 最后锁定输出格式\n\n"
            f"## 练习建议\n"
            f"- 把 `{topic}` 换成别的主题\n"
            f"- 去掉一个约束后重新运行\n"
            f"- 观察输出是否变得更散\n"
        )

    return (
        f"关于 {topic}，你可以先了解它是什么，然后看看相关概念，再试着自己动手。\n"
        f"不过这个回答还没有固定结构，后续很难直接放进页面里。"
    )


def build_loose_chain():
    prompt = PromptTemplate.from_template(
        "请介绍一下主题：{topic}"
    )
    return prompt | RunnableLambda(toy_model)


def build_controlled_chain():
    prompt = PromptTemplate.from_template(
        "你是一个中文 LangChain 学习助手。\n"
        "目标读者：初学者\n"
        "主题：{topic}\n"
        "要求：\n"
        "1. 固定 4 个部分\n"
        "2. 使用 Markdown 小标题\n"
        "3. 每部分都简洁\n"
        "4. 不要输出与主题无关的内容\n"
        "5. 输出适合网页渲染\n"
    )
    return prompt | RunnableLambda(toy_model)


def main() -> None:
    topic = "Prompt 工程与输出控制"

    print("=== Loose Prompt ===")
    loose_result = build_loose_chain().invoke({"topic": topic})
    print(loose_result)

    print()
    print("=== Controlled Prompt ===")
    controlled_result = build_controlled_chain().invoke({"topic": topic})
    print(controlled_result)


if __name__ == "__main__":
    main()
