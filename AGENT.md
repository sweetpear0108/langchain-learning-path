# AGENT.md

## Purpose

This repository is a chapter-based, project-driven LangChain learning site for Chinese-speaking developers.

The project has two primary source documents:

- [docs/DESIGN.md](./docs/DESIGN.md)
- [docs/COURSE_OUTLINE.md](./docs/COURSE_OUTLINE.md)

This file is the short operational brief for humans and coding agents working in the repo.

## Source Of Truth

When there is ambiguity, follow this order:

1. `docs/DESIGN.md`
2. `docs/COURSE_OUTLINE.md`
3. Existing repository structure and naming

Do not invent a different product direction without updating the design docs.

## Product Summary

The repository should evolve into:

- A public learning site deployed on `GitHub Pages`
- A structured LangChain learning path
- A project-driven tutorial centered on one evolving app: `AI 学习助手`

The product is not a generic note dump and not just a demo collection. It must combine:

- Structured curriculum
- Progressive project implementation
- Public-facing learning experience

## Delivery Strategy

The project follows two phases.

### Phase 1

Build a static documentation site first.

Primary goals:

- Publish a stable tutorial site
- Establish the learning path
- Provide chapter content, diagrams, examples, and exercises

### Phase 2

Add an external backend for interactive experiments.

Primary goals:

- Run LangChain workflows safely outside GitHub Pages
- Add chapter-based playground pages
- Support RAG, tools, agents, and LangGraph demos

## Curriculum Summary

The full outline lives in `docs/COURSE_OUTLINE.md`. The intended chapter progression is:

1. LLM 应用基础
2. LangChain 核心抽象
3. 第一个链式应用
4. Prompt 工程与输出控制
5. RAG 入门
6. RAG 进阶优化
7. Tools 与 Agent
8. LangGraph 工作流
9. 评估、观测与调试
10. 综合实战与公开部署

All chapters should reinforce the same evolving project: `AI 学习助手`.

## Repository Intent

Expected top-level responsibilities:

- `docs/`: documentation site content
- `examples/`: chapter-specific runnable examples
- `backend/`: phase-2 API and LangChain runtime
- `shared/`: prompts, datasets, diagrams, and shared assets
- `.github/workflows/`: automation and deployment

## Content Rules

Each chapter should aim to include:

- Learning goals
- Prerequisites
- Core concepts
- Minimal runnable example
- Code walkthrough
- Diagram or flow explanation
- Exercises
- Common pitfalls
- Chapter summary

The teaching style should stay practical:

- Start from a minimal working implementation
- Explain why each abstraction exists
- Avoid dumping large blocks of theory first
- Keep the learning path incremental

## Technical Defaults

Default stack unless design docs are updated:

- Documentation site: `VitePress`
- Example language: `Python`
- Interactive backend: `FastAPI`
- Public deployment target for docs: `GitHub Pages`

## Priority Order

If the repo is still in early setup, build in this order:

1. Documentation site skeleton
2. Homepage and roadmap page
3. Chapter 1 and Chapter 2 content
4. Runnable examples for early chapters
5. GitHub Pages deployment workflow
6. Remaining chapters
7. Interactive backend

## Editing Guidance

- Preserve the chapter-first information architecture
- Keep naming clear and predictable
- Prefer adding small, complete units over large unfinished scaffolds
- If you change product scope, update `docs/DESIGN.md`
- If you change course sequencing, update `docs/COURSE_OUTLINE.md`

## Definition Of Done

Work is in good shape when:

- The repository structure matches the design direction
- Docs and examples are aligned
- New content fits the chapter template
- The public site can eventually be built and deployed cleanly

## Immediate Next Steps

The most valuable next implementation tasks are:

1. Initialize the VitePress site
2. Create `docs/index.md`
3. Create the roadmap page
4. Draft Chapter 1 and Chapter 2 pages
5. Add example code under `examples/chapter-01` and `examples/chapter-02`
