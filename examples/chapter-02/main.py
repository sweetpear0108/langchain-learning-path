from dataclasses import dataclass
from typing import Any, Dict


class Runnable:
    def __or__(self, other: "Runnable") -> "Pipeline":
        return Pipeline(self, other)

    def invoke(self, value: Any) -> Any:
        raise NotImplementedError


class Pipeline(Runnable):
    def __init__(self, left: Runnable, right: Runnable) -> None:
        self.left = left
        self.right = right

    def invoke(self, value: Any) -> Any:
        return self.right.invoke(self.left.invoke(value))


@dataclass
class PromptTemplate(Runnable):
    template: str

    def invoke(self, value: Dict[str, Any]) -> str:
        return self.template.format(**value)


class DemoModel(Runnable):
    def invoke(self, prompt: str) -> str:
        return (
            "标题: LangChain 核心抽象\n"
            "学习目标: 理解 PromptTemplate、Model 和 Parser 的职责\n"
            "核心概念: PromptTemplate, Runnable, LCEL\n"
            "学习顺序: 先理解 PromptTemplate，再看模型，再接 Parser\n"
            "练习建议: 用自己的话解释为什么链路要拆分"
        )


class StructuredParser(Runnable):
    def invoke(self, text: str) -> Dict[str, str]:
        result: Dict[str, str] = {}
        for line in text.splitlines():
            if ": " not in line:
                continue
            key, value = line.split(": ", 1)
            result[key.strip()] = value.strip()
        return result


def pretty_print(value: Any) -> str:
    if isinstance(value, dict):
        return "\n".join(f"- {key}: {val}" for key, val in value.items())
    return str(value)


def main() -> None:
    prompt = PromptTemplate(
        template=("你是一个中文 AI 学习助手。\n请围绕主题 {topic} 输出一份结构化摘要。")
    )
    model = DemoModel()
    parser = StructuredParser()

    chain = prompt | model | parser
    result = chain.invoke({"topic": "LangChain 核心抽象"})

    print("=== PromptTemplate Output ===")
    print(prompt.invoke({"topic": "LangChain 核心抽象"}))
    print()
    print("=== Parsed Result ===")
    print(pretty_print(result))


if __name__ == "__main__":
    main()
