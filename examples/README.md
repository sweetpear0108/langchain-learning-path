# Examples

这里存放 10 个章节对应的最小可运行示例。

## 目录结构

- `chapter-01`：LLM 应用基础
- `chapter-02`：LangChain 核心抽象
- `chapter-03`：第一个链式应用
- `chapter-04`：Prompt 工程与输出控制
- `chapter-05`：RAG 入门
- `chapter-06`：RAG 进阶优化
- `chapter-07`：Tools 与 Agent
- `chapter-08`：LangGraph 工作流
- `chapter-09`：评估、观测与调试
- `chapter-10`：综合实战与公开部署

## 使用方式

优先阅读每个章节目录下的 `README.md`。

典型流程：

```bash
cd examples/chapter-03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

如果某一章不需要第三方依赖，会在该章节的 `README.md` 中直接说明。
