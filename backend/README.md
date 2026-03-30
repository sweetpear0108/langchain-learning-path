# Backend

这里现在提供一个 `Phase 2` 的最小可见成果：`FastAPI` 骨架已经建立，但它仍然只是占位后端，不代表在线实验能力已经完成。

当前已包含：

- `backend/app/main.py` 中的最小 `FastAPI` 应用
- `GET /health` 健康检查路由
- `GET /demo` 占位演示接口，用于说明未来后端会承载什么能力

当前未包含：

- 真实模型调用
- LangChain / LangGraph 运行时
- RAG、Tools、Agent 等在线实验接口
- 鉴权、持久化、任务队列等工程能力

计划职责：

- 模型调用代理
- LangChain 运行逻辑
- RAG / Agent / LangGraph 实验接口

本地启动：

```bash
python -m pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```
