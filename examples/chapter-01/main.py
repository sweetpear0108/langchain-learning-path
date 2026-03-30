from dataclasses import dataclass


@dataclass
class ToyLLM:
    """A tiny stand-in for a real model client."""

    model_name: str = "toy-llm"

    def generate(self, prompt: str) -> str:
        if "LangChain" in prompt:
            topic = "LangChain"
        elif "RAG" in prompt:
            topic = "RAG"
        else:
            topic = "这个主题"

        return (
            f"学习目标：理解 {topic} 的核心概念。\n"
            f"核心概念：输入、Prompt、模型、输出。\n"
            f"学习顺序：先看定义，再看示例，再做练习。\n"
            f"练习建议：用一段话复述 {topic} 的作用，并写出自己的理解。"
        )


def build_prompt(topic: str, audience: str = "初学者") -> str:
    return (
        "你是一个中文 AI 学习助手。\n"
        f"目标读者：{audience}\n"
        f"任务：围绕主题 {topic} 生成一份简洁学习摘要。\n"
        "要求：\n"
        "1. 输出学习目标\n"
        "2. 输出核心概念\n"
        "3. 输出学习顺序\n"
        "4. 输出练习建议\n"
        "5. 不要输出无关内容\n"
    )


def main() -> None:
    topic = "LangChain 应用基础"
    prompt = build_prompt(topic)
    model = ToyLLM()
    result = model.generate(prompt)

    print("=== Prompt ===")
    print(prompt)
    print()
    print("=== Model Output ===")
    print(result)


if __name__ == "__main__":
    main()
