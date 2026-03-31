---
layout: home

hero:
  name: LangChain Learning Path
  text: 用一个主项目，把 LangChain 从基础一路学到可部署
  tagline: 面向中文开发者的章节化学习站。你不只是看概念，而是沿着 AI 学习助手这条主线，逐章完成 Prompt、链、RAG、Agent、LangGraph 和部署。
  actions:
    - theme: brand
      text: 从新手 Setup 进入
      link: /guide/setup
    - theme: alt
      text: 直接看章节
      link: /chapters/
    - theme: alt
      text: 查看路线图
      link: /guide/roadmap

features:
  - title: 一条稳定主线
    details: 不是零散知识点堆叠，而是围绕 AI 学习助手逐步升级，始终知道自己在做什么。
  - title: 每章都有落点
    details: 每一章都包含目标、概念、最小示例、常见坑、练习题和下一步。
  - title: 先做出来，再学抽象
    details: 整个项目坚持先跑通最小实现，再理解为什么需要 LangChain、RAG、Agent 和 LangGraph。
---

<div class="section-callout">
  <strong>适合谁：</strong>
  已有 Python 基础，想系统学 LangChain；不想再靠零散博客拼知识；希望做出一个可以公开展示、部署和持续迭代的 AI 应用。
</div>

## 快速导航

<p class="nav-intro">
  顶栏已经按「开始学习 / 课程与项目 / 支持与参考」收敛。第一次进入站点时，可以先从下面的入口区判断自己现在最需要去哪一类页面。
</p>

<div class="nav-overview">
  <section class="nav-panel">
    <span class="nav-card-kicker">Start Here</span>
    <h3>开始学习</h3>
    <p>适合第一次进入仓库的读者，先完成环境准备，再建立阅读顺序和学习节奏。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="/guide/setup">
        <strong>新手 Setup</strong>
        <span>先把文档站和第一个示例跑起来。</span>
      </a>
      <a class="nav-link-item" href="/guide/getting-started">
        <strong>快速开始</strong>
        <span>理解这套学习站怎么读、先看什么。</span>
      </a>
      <a class="nav-link-item" href="/guide/study-plan">
        <strong>学习计划</strong>
        <span>按 7 天、14 天、30 天节奏安排学习。</span>
      </a>
    </div>
  </section>
  <section class="nav-panel">
    <span class="nav-card-kicker">Core Paths</span>
    <h3>课程与项目</h3>
    <p>适合已经开始系统学习的人，直接进入章节、主项目和示例代码三条主线。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="/chapters/">
        <strong>章节目录</strong>
        <span>从第 1 章到第 10 章按顺序推进。</span>
      </a>
      <a class="nav-link-item" href="/project/">
        <strong>主项目</strong>
        <span>跟着 AI 学习助手的版本演进理解能力落点。</span>
      </a>
      <a class="nav-link-item" href="/examples/">
        <strong>示例代码</strong>
        <span>查看每章对应的最小可运行示例。</span>
      </a>
      <a class="nav-link-item" href="/compare/">
        <strong>方法对比</strong>
        <span>建立 Chain、Agent、RAG、LangGraph 的选择判断。</span>
      </a>
    </div>
  </section>
  <section class="nav-panel">
    <span class="nav-card-kicker">Support</span>
    <h3>支持与参考</h3>
    <p>适合查概念、解问题和补背景，减少在章节之间反复跳转的成本。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="/guide/roadmap">
        <strong>学习路线图</strong>
        <span>先看整体教学路径和阶段目标。</span>
      </a>
      <a class="nav-link-item" href="/faq/glossary">
        <strong>术语表</strong>
        <span>快速回查 Runnable、Retriever、Trace 等高频术语。</span>
      </a>
      <a class="nav-link-item" href="/faq/">
        <strong>FAQ</strong>
        <span>集中查看常见问题和排查入口。</span>
      </a>
      <a class="nav-link-item" href="/faq/troubleshooting">
        <strong>故障排查</strong>
        <span>遇到环境或构建问题时，直接查看定位建议。</span>
      </a>
    </div>
  </section>
</div>

## 学习路径一览

<div class="path-grid">
  <div class="path-card">
    <h3>基础层</h3>
    <p>先建立 LLM 应用视角，再理解 Prompt、Model、Parser、Runnable 和 LCEL 这些最核心抽象。</p>
  </div>
  <div class="path-card">
    <h3>应用层</h3>
    <p>从第一个链式应用开始，进入 Prompt 工程、RAG 和检索优化，把 AI 学习助手真正做起来。</p>
  </div>
  <div class="path-card">
    <h3>编排层</h3>
    <p>当流程开始变复杂，再引入 Tools、Agent 和 LangGraph，让系统从能跑升级到可控。</p>
  </div>
  <div class="path-card">
    <h3>工程层</h3>
    <p>最后补评估、观测、调试和公开部署，把项目打磨成可以分享给别人的作品。</p>
  </div>
</div>

## 你会沿着什么项目学习

整个站点围绕一个持续演进的主项目：`AI 学习助手`。

<div class="timeline-list">
  <div class="timeline-item">
    <strong>V1</strong>
    从最小链式应用开始，只做主题摘要和学习顺序建议。
  </div>
  <div class="timeline-item">
    <strong>V2</strong>
    通过 Prompt 工程和结构化输出，让结果更稳定、更适合渲染。
  </div>
  <div class="timeline-item">
    <strong>V3</strong>
    接入课程资料，升级为可回答资料内容的基础 RAG 学习助手。
  </div>
  <div class="timeline-item">
    <strong>V4</strong>
    引入 Tools、Agent 和 LangGraph，把系统组织成更完整的工作流。
  </div>
  <div class="timeline-item">
    <strong>最终形态</strong>
    文档站 + 示例代码 + 可扩展后端，一套能公开展示的 LangChain 学习项目。
  </div>
</div>

## 推荐入口

<div class="quick-links">
  <a href="/guide/setup">新手 Setup</a>
  <a href="/guide/getting-started">快速开始</a>
  <a href="/compare/">方法对比页</a>
  <a href="/guide/roadmap">学习路线图</a>
  <a href="/faq/glossary">术语表</a>
  <a href="/chapters/">章节目录</a>
  <a href="/project/">主项目演进</a>
  <a href="/faq/">FAQ</a>
</div>

第一次进入本项目，建议先看：

1. [新手 Setup](./guide/setup.md)
2. [快速开始](./guide/getting-started.md)
3. [学习路线图](./guide/roadmap.md)

如果想理解这套项目为什么这样设计，再看：

- [完整设计方案](./DESIGN.md)
- [完整课程大纲](./COURSE_OUTLINE.md)

如果已经开始做项目，想先建立“什么时候该选哪种方法”的判断，再看：

- [方法对比页](./compare/README.md)
