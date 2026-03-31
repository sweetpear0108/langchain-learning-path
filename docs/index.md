---
layout: home

hero:
  name: LangChain Learning Path
  text: 一条主线学会 LangChain、RAG、Agent 和 LangGraph
  tagline: 围绕 AI 学习助手，把学习顺序、章节内容、示例代码和部署边界放在同一条线上，先看主线，再决定进入哪一页。
  actions:
    - theme: brand
      text: 从新手 Setup 进入
      link: /guide/setup
    - theme: alt
      text: 查看章节目录
      link: /chapters/
    - theme: alt
      text: 查看学习路线图
      link: /guide/roadmap
---

<div class="home-poster">
  <div class="home-poster-copy">
    <p class="home-kicker">首页总览</p>
    <h2>把学习入口、章节主线和项目边界压成一张清晰的路线图。</h2>
    <p class="home-lead">
      这里不是卡片集合式导航，而是一个先判断方向、再进入内容的扁平首页：先知道学什么，再知道为什么学，最后才进入具体页面。
    </p>
    <div class="home-facts">
      <div>
        <span>学习入口</span>
        <strong>新手 Setup / 快速开始 / 路线图</strong>
      </div>
      <div>
        <span>章节主线</span>
        <strong>基础层 / 应用层 / 编排层 / 工程层</strong>
      </div>
      <div>
        <span>项目边界</span>
        <strong>围绕 AI 学习助手逐章演进</strong>
      </div>
    </div>
  </div>
  <aside class="home-poster-board">
    <p class="home-board-label">当前站点结构</p>
    <ul>
      <li><strong>首页</strong> 先回答这是什么、从哪里开始。</li>
      <li><strong>章节目录</strong> 按 10 章递进建立能力。</li>
      <li><strong>主项目</strong> 用同一个 AI 学习助手串起所有章节。</li>
      <li><strong>支持页</strong> 提供 FAQ、术语表和排查入口。</li>
    </ul>
  </aside>
</div>

## 直接进入

<p class="nav-intro">
  顶部导航只保留四个明确入口，首页下面再把它们展开成一张平面的信息地图。你可以先按当前状态选择入口，而不是在多个相似卡片之间反复比较。
</p>

<div class="nav-overview">
  <section class="nav-panel">
    <span class="nav-card-kicker">Start Here</span>
    <h3>开始学习</h3>
    <p>先把环境、阅读顺序和基础节奏理顺，再进入正式章节。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="./guide/setup">
        <strong>新手 Setup</strong>
        <span>先完成最小可运行环境与站点浏览。</span>
      </a>
      <a class="nav-link-item" href="./guide/getting-started">
        <strong>快速开始</strong>
        <span>快速理解这套学习站的阅读方式。</span>
      </a>
      <a class="nav-link-item" href="./guide/study-plan">
        <strong>学习计划</strong>
        <span>按 7 天、14 天、30 天节奏安排学习。</span>
      </a>
    </div>
  </section>
  <section class="nav-panel">
    <span class="nav-card-kicker">Core Paths</span>
    <h3>课程与项目</h3>
    <p>章节、主项目和示例代码是同一条主线上的不同视角。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="./chapters/">
        <strong>章节目录</strong>
        <span>从第 1 章到第 10 章按顺序推进。</span>
      </a>
      <a class="nav-link-item" href="./project/">
        <strong>主项目</strong>
        <span>跟着 AI 学习助手的版本演进理解能力落点。</span>
      </a>
      <a class="nav-link-item" href="./examples/">
        <strong>示例代码</strong>
        <span>查看每章对应的最小可运行示例。</span>
      </a>
      <a class="nav-link-item" href="./compare/">
        <strong>方法对比</strong>
        <span>建立 Chain、Agent、RAG、LangGraph 的选择判断。</span>
      </a>
    </div>
  </section>
  <section class="nav-panel">
    <span class="nav-card-kicker">Support</span>
    <h3>支持与参考</h3>
    <p>概念、术语和问题排查集中放在这里，减少在章节之间反复跳转的成本。</p>
    <div class="nav-link-list">
      <a class="nav-link-item" href="./guide/roadmap">
        <strong>学习路线图</strong>
        <span>先看整体教学路径和阶段目标。</span>
      </a>
      <a class="nav-link-item" href="./faq/glossary">
        <strong>术语表</strong>
        <span>快速回查 Runnable、Retriever、Trace 等高频术语。</span>
      </a>
      <a class="nav-link-item" href="./faq/">
        <strong>FAQ</strong>
        <span>集中查看常见问题和排查入口。</span>
      </a>
      <a class="nav-link-item" href="./faq/troubleshooting">
        <strong>故障排查</strong>
        <span>遇到环境或构建问题时，直接查看定位建议。</span>
      </a>
    </div>
  </section>
</div>

## 学习路径

<div class="path-strip">
  <div class="path-step">
    <span class="path-step-index">01</span>
    <div>
      <h3>基础层</h3>
      <p>先建立 LLM 应用视角，再理解 Prompt、Model、Parser、Runnable 和 LCEL。</p>
    </div>
  </div>
  <div class="path-step">
    <span class="path-step-index">02</span>
    <div>
      <h3>应用层</h3>
      <p>从第一个链式应用开始，进入 Prompt 工程、RAG 和检索优化。</p>
    </div>
  </div>
  <div class="path-step">
    <span class="path-step-index">03</span>
    <div>
      <h3>编排层</h3>
      <p>当流程变复杂时，引入 Tools、Agent 和 LangGraph，让系统可控。</p>
    </div>
  </div>
  <div class="path-step">
    <span class="path-step-index">04</span>
    <div>
      <h3>工程层</h3>
      <p>补上评估、观测、调试和公开部署，把项目打磨成可分享作品。</p>
    </div>
  </div>
</div>

## 主项目演进

<p class="nav-intro">
  整个站点围绕一个持续演进的主项目：<code>AI 学习助手</code>。每一章只推进一个明确能力，避免每章换一个无关 Demo。
</p>

<div class="project-line">
  <div class="project-stage">
    <strong>V1</strong>
    <span>最小链式应用，只做主题摘要和学习顺序建议。</span>
  </div>
  <div class="project-stage">
    <strong>V2</strong>
    <span>通过 Prompt 工程和结构化输出，让结果更稳定。</span>
  </div>
  <div class="project-stage">
    <strong>V3</strong>
    <span>接入课程资料，升级为基础 RAG 学习助手。</span>
  </div>
  <div class="project-stage">
    <strong>V4</strong>
    <span>引入 Tools、Agent 和 LangGraph，把系统组织成完整工作流。</span>
  </div>
</div>

## 推荐入口

<div class="quick-links">
  <a href="./guide/setup">新手 Setup</a>
  <a href="./guide/getting-started">快速开始</a>
  <a href="./guide/roadmap">学习路线图</a>
  <a href="./chapters/">章节目录</a>
  <a href="./project/">主项目演进</a>
  <a href="./examples/">示例代码</a>
  <a href="./faq/glossary">术语表</a>
  <a href="./faq/">FAQ</a>
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
