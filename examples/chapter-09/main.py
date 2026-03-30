from __future__ import annotations

import argparse
import json
import time
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class EvalCase:
    id: str
    question: str
    expected_points: list[str]
    scenario: str
    priority: int


@dataclass(frozen=True)
class TraceEvent:
    stage: str
    detail: str
    at_ms: int


@dataclass
class AnswerResult:
    case_id: str
    route: str
    answer: str
    trace: list[TraceEvent]


EVAL_CASES = [
    EvalCase(
        id="basic-01",
        question="什么是 LangChain 的 Runnable？",
        expected_points=["可组合", "统一接口", "链式执行"],
        scenario="core-concept",
        priority=1,
    ),
    EvalCase(
        id="rag-01",
        question="为什么 RAG 能降低幻觉？",
        expected_points=["检索外部知识", "基于资料回答", "减少纯生成猜测"],
        scenario="rag",
        priority=1,
    ),
    EvalCase(
        id="agent-01",
        question="什么时候应该用 Agent 而不是固定链？",
        expected_points=["动态决策", "多工具", "流程不固定"],
        scenario="agent",
        priority=2,
    ),
    EvalCase(
        id="debug-01",
        question="如果回答偏题，第一步该看什么？",
        expected_points=["输入", "检索", "上下文", "输出格式"],
        scenario="debugging",
        priority=2,
    ),
]


class DemoLearningAssistant:
    def answer(self, question: str) -> AnswerResult:
        started = time.perf_counter()
        trace: list[TraceEvent] = [self._trace("input", question, started)]
        route = self._route(question)
        trace.append(self._trace("route", route, started))

        answer = self._generate_answer(question, route)
        trace.append(self._trace("answer", answer, started))

        return AnswerResult(case_id="", route=route, answer=answer, trace=trace)

    def _route(self, question: str) -> str:
        q = question.lower()
        if "rag" in q or "检索" in q:
            return "rag"
        if "agent" in q or "工具" in q:
            return "agent"
        if "调试" in q or "trace" in q or "评估" in q or "偏题" in q:
            return "debug"
        return "core"

    def _generate_answer(self, question: str, route: str) -> str:
        if route == "rag":
            return "RAG 通过检索外部知识，让模型基于资料回答，从而减少纯生成猜测。"
        if route == "agent":
            return (
                "Agent 适合流程不固定、需要动态决策和多工具协作的任务；"
                "如果流程已经固定，优先使用链。"
            )
        if route == "debug":
            return (
                "调试时先看输入，再看检索，再看上下文，最后检查输出格式。"
                "把 trace 记录下来，问题会更容易定位。"
            )
        return (
            "Runnable 提供可组合、统一接口和链式执行能力，"
            "适合把 Prompt、Model、Parser 串成稳定的链式流程。"
        )

    @staticmethod
    def _trace(stage: str, detail: str, started: float) -> TraceEvent:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        return TraceEvent(stage=stage, detail=detail, at_ms=elapsed_ms)


def score_answer(answer: str, expected_points: list[str]) -> tuple[int, list[str]]:
    score = 0
    missing: list[str] = []
    for point in expected_points:
        if point in answer:
            score += 1
        else:
            missing.append(point)
    return score, missing


def run_eval(cases: list[EvalCase], assistant: DemoLearningAssistant) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for case in cases:
        result = assistant.answer(case.question)
        result.case_id = case.id
        score, missing = score_answer(result.answer, case.expected_points)
        results.append(
            {
                "id": case.id,
                "scenario": case.scenario,
                "priority": case.priority,
                "route": result.route,
                "score": score,
                "max_score": len(case.expected_points),
                "missing": missing,
                "answer": result.answer,
                "trace": [asdict(event) for event in result.trace],
            }
        )
    return results


def print_report(results: list[dict[str, object]]) -> None:
    print("# Evaluation Report")
    print()
    for item in results:
        missing = ", ".join(item["missing"]) if item["missing"] else "-"
        print(
            f"- {item['id']} | route={item['route']} | "
            f"score={item['score']}/{item['max_score']} | missing={missing}"
        )
        print(f"  answer: {item['answer']}")
        trace_excerpt = json.dumps(item["trace"], ensure_ascii=False)
        print(f"  trace: {trace_excerpt}")
    print()
    total = sum(int(item["score"]) for item in results)
    max_total = sum(int(item["max_score"]) for item in results)
    print(f"Overall score: {total}/{max_total}")


def select_cases(case_id: str | None) -> list[EvalCase]:
    if not case_id:
        return EVAL_CASES
    selected = [case for case in EVAL_CASES if case.id == case_id]
    if not selected:
        available = ", ".join(case.id for case in EVAL_CASES)
        raise SystemExit(f"Unknown case id: {case_id}. Available: {available}")
    return selected


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the chapter 9 evaluation demo.")
    parser.add_argument("--case", help="Run one specific eval case by id.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    assistant = DemoLearningAssistant()
    results = run_eval(select_cases(args.case), assistant)
    print_report(results)


if __name__ == "__main__":
    main()
