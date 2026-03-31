from typing import Callable, TypedDict

from langgraph.graph import END, START, StateGraph

State = dict[str, str]


def classify(state: State) -> State:
    question = state["question"]
    if "目录" in question or "第几章" in question or "先学" in question:
        state["route"] = "outline"
    elif "练习" in question:
        state["route"] = "practice"
    elif "不清楚" in question or "快速" in question:
        state["route"] = "clarify"
    else:
        state["route"] = "rag"
    state["trace"] += " -> classify"
    return state


def retrieve(state: State) -> State:
    state["context"] = "检索到课程资料：第 7 章讲 Tool/Agent，第 8 章讲工作流编排。"
    state["trace"] += " -> retrieve"
    return state


def outline_lookup(state: State) -> State:
    state["context"] = "课程目录：1-10 章按基础、RAG、Agent、LangGraph、部署递进。"
    state["trace"] += " -> outline_lookup"
    return state


def clarify(state: State) -> State:
    state["context"] = "请补充你的目标：你是想先看路线图，还是想先看某一章的实战示例？"
    state["trace"] += " -> clarify"
    return state


def summarize(state: State) -> State:
    if state.get("route") == "practice":
        state["answer"] = "给出 3 道练习题：设计节点、设计状态、设计兜底路径。"
    else:
        state["answer"] = f"基于上下文回答：{state.get('context', '')}"
    state["trace"] += " -> summarize"
    return state


def build_graph() -> dict[str, Callable[[State], State]]:
    return {
        "classify": classify,
        "retrieve": retrieve,
        "outline": outline_lookup,
        "clarify": clarify,
        "summarize": summarize,
    }


def run_graph(question: str) -> State:
    graph = build_graph()
    state: State = {
        "question": question,
        "route": "",
        "context": "",
        "answer": "",
        "trace": "start",
    }

    state = graph["classify"](state)

    if state["route"] == "outline":
        state = graph["outline"](state)
        state = graph["summarize"](state)
    elif state["route"] == "clarify":
        state = graph["clarify"](state)
    else:
        state = graph["retrieve"](state)
        state = graph["summarize"](state)

    return state


def main() -> None:
    questions = [
        "我想查一下第 7 章需要先学什么",
        "给我第 8 章的练习题",
        "我想快速学会这个项目",
    ]

    print("Chapter 08: LangGraph 工作流")
    print("主项目：AI 学习助手 V4")
    print()

    for question in questions:
        state = run_graph(question)
        print("== 教学版 ==")
        print(f"Q: {state['question']}")
        print(f"route: {state['route']}")
        print(f"trace: {state['trace']}")
        if state["route"] == "clarify":
            print(f"clarify: {state['context']}")
        else:
            print(f"context: {state['context']}")
            print(f"answer: {state['answer']}")
        print()

    print("== 真实框架版 ==")
    graph = build_real_graph()
    for question in questions:
        state = graph.invoke(
            {
                "question": question,
                "route": "",
                "context": "",
                "answer": "",
                "trace": "start",
            }
        )
        print(f"Q: {state['question']}")
        print(f"route: {state['route']}")
        print(f"trace: {state['trace']}")
        print(f"context: {state['context']}")
        print(f"answer: {state['answer']}")
        print()


class WorkflowState(TypedDict):
    question: str
    route: str
    context: str
    answer: str
    trace: str


def real_classify(state: WorkflowState) -> WorkflowState:
    if "第 7 章" in state["question"]:
        route = "outline"
    elif "快速" in state["question"]:
        route = "clarify"
    else:
        route = "rag"
    return {"route": route, "trace": f"{state['trace']} -> classify"}


def real_outline(state: WorkflowState) -> WorkflowState:
    return {
        "context": "目录节点命中了课程结构：先学第 2、3、5 章，再进入第 7 章。",
        "answer": "建议按基础抽象 -> 第一个链 -> RAG 入门 -> Tools 与 Agent 的顺序推进。",
        "trace": f"{state['trace']} -> outline",
    }


def real_rag(state: WorkflowState) -> WorkflowState:
    return {
        "context": "RAG 节点命中了课程资料：第 8 章强调状态、节点和条件分支。",
        "answer": "这类问题适合先检索相关章节，再由总结节点整理答案。",
        "trace": f"{state['trace']} -> rag",
    }


def real_clarify(state: WorkflowState) -> WorkflowState:
    return {
        "context": "澄清节点要求补充目标：你是想看路线图，还是想直接看实战示例？",
        "answer": "需要先澄清，再继续流转。",
        "trace": f"{state['trace']} -> clarify",
    }


def select_route(state: WorkflowState) -> str:
    return state["route"]


def build_real_graph():
    builder = StateGraph(WorkflowState)
    builder.add_node("classify", real_classify)
    builder.add_node("outline", real_outline)
    builder.add_node("rag", real_rag)
    builder.add_node("clarify", real_clarify)
    builder.add_edge(START, "classify")
    builder.add_conditional_edges(
        "classify",
        select_route,
        {"outline": "outline", "rag": "rag", "clarify": "clarify"},
    )
    builder.add_edge("outline", END)
    builder.add_edge("rag", END)
    builder.add_edge("clarify", END)
    return builder.compile()


if __name__ == "__main__":
    main()
