from dataclasses import dataclass
from typing import Callable, Dict, List

from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool


@dataclass
class Tool:
    name: str
    description: str
    handler: Callable[[str], str]


def search_outline(query: str) -> str:
    chapters = {
        "1": "第 1 章：LLM 应用基础",
        "2": "第 2 章：LangChain 核心抽象",
        "7": "第 7 章：Tools 与 Agent",
        "8": "第 8 章：LangGraph 工作流",
    }
    if query in chapters:
        return f"{chapters[query]} | 摘要：理解工具调用和动态决策。"
    return "未找到对应章节，请输入章节编号，例如 7。"


def get_chapter_summary(query: str) -> str:
    summaries = {
        "7": "Tools 让模型可以调用外部能力，Agent 让模型可以选择调用哪个工具。",
        "8": "LangGraph 把复杂流程显式建模为状态图，便于分支、循环和恢复。",
    }
    return summaries.get(query, "暂无该章节摘要。")


def generate_practice(query: str) -> str:
    return (
        f"围绕 {query} 的练习题：\n"
        "1. 设计一个输入明确、输出稳定的 Tool。\n"
        "2. 说明为什么这个任务适合 Agent，而不是固定链。\n"
        "3. 写出一个错误处理策略。"
    )


TOOLS: List[Tool] = [
    Tool("search_outline", "查询课程目录", search_outline),
    Tool("get_chapter_summary", "获取章节摘要", get_chapter_summary),
    Tool("generate_practice", "生成练习题", generate_practice),
]


@tool
def search_outline_tool(chapter: str) -> str:
    """Query the course outline for a chapter number."""
    return search_outline(chapter)


@tool
def get_chapter_summary_tool(chapter: str) -> str:
    """Read the summary for a chapter number."""
    return get_chapter_summary(chapter)


@tool
def generate_practice_tool(topic: str) -> str:
    """Generate practice questions for a topic."""
    return generate_practice(topic)


REAL_TOOLS = [
    search_outline_tool,
    get_chapter_summary_tool,
    generate_practice_tool,
]
REAL_TOOL_REGISTRY = {tool_item.name: tool_item for tool_item in REAL_TOOLS}


def route_question(question: str) -> Dict[str, str]:
    lower = question.lower()
    if "练习" in question or "题目" in question:
        return {"tool": "generate_practice", "input": "Tools 与 Agent"}
    if "前置" in question or "先学" in question or "目录" in question:
        return {"tool": "search_outline", "input": "7"}
    if "第 7 章" in question or "第7章" in question or "chapter 7" in lower:
        return {"tool": "get_chapter_summary", "input": "7"}
    return {"tool": "", "input": ""}


def agent_respond(question: str) -> str:
    decision = route_question(question)
    if not decision["tool"]:
        return (
            "我暂时无法直接判断需要哪个工具。\n"
            "你可以把问题缩小为：\n"
            "- 查询某一章摘要\n"
            "- 查询课程目录\n"
            "- 生成某个主题的练习题"
        )

    tool = next(t for t in TOOLS if t.name == decision["tool"])
    tool_result = tool.handler(decision["input"])
    return f"Agent 选择了工具 `{tool.name}`：\n{tool_result}"


def plan_tool_calls(question: str) -> AIMessage:
    if "前置" in question or "先学" in question:
        return AIMessage(
            content="",
            tool_calls=[
                {
                    "name": "search_outline_tool",
                    "args": {"chapter": "7"},
                    "id": "call-outline-7",
                    "type": "tool_call",
                },
                {
                    "name": "get_chapter_summary_tool",
                    "args": {"chapter": "7"},
                    "id": "call-summary-7",
                    "type": "tool_call",
                },
            ],
        )
    if "练习" in question or "题目" in question:
        return AIMessage(
            content="",
            tool_calls=[
                {
                    "name": "generate_practice_tool",
                    "args": {"topic": "Tools 与 Agent"},
                    "id": "call-practice-7",
                    "type": "tool_call",
                }
            ],
        )
    return AIMessage(content="这个问题更适合先澄清需求，当前不发起工具调用。", tool_calls=[])


def execute_tool_calls(tool_calls: list[dict]) -> list[ToolMessage]:
    messages: list[ToolMessage] = []
    for tool_call in tool_calls:
        selected_tool = REAL_TOOL_REGISTRY[tool_call["name"]]
        result = selected_tool.invoke(tool_call["args"])
        messages.append(
            ToolMessage(
                content=result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return messages


def summarize_tool_messages(question: str, tool_messages: list[ToolMessage]) -> str:
    if not tool_messages:
        return "没有触发工具。建议把问题缩小到章节查询、摘要读取或练习生成。"
    evidence = "\n".join(f"- {message.name}: {message.content}" for message in tool_messages)
    return f"问题：{question}\n工具证据：\n{evidence}\n最终答复：先看课程结构，再结合章节摘要安排练习。"


def demo_tools() -> None:
    print("== Tool 演示 ==")
    for tool in TOOLS:
        print(f"- {tool.name}: {tool.description}")
    print()
    print(search_outline("7"))
    print(get_chapter_summary("7"))
    print(generate_practice("Tools 与 Agent"))
    print()


def demo_agent() -> None:
    questions = [
        "我想先学第 7 章，需要什么前置知识？",
        "给我三道第 7 章的练习题",
        "这个项目怎么学比较快？",
    ]
    print("== Agent 演示 ==")
    for question in questions:
        print(f"Q: {question}")
        print(agent_respond(question))
        print()


def demo_real_framework() -> None:
    questions = [
        "我想先学第 7 章，需要什么前置知识？",
        "给我三道第 7 章的练习题",
    ]
    print("== 真实框架版 ==")
    for question in questions:
        ai_message = plan_tool_calls(question)
        tool_messages = execute_tool_calls(ai_message.tool_calls)
        print(f"Q: {question}")
        print(f"planned tool calls: {ai_message.tool_calls}")
        for tool_message in tool_messages:
            print(f"tool[{tool_message.name}]: {tool_message.content}")
        print(summarize_tool_messages(question, tool_messages))
        print()


if __name__ == "__main__":
    print("Chapter 07: Tools 与 Agent")
    print("主项目：AI 学习助手 V3")
    print()
    demo_tools()
    demo_agent()
    demo_real_framework()
