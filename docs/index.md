---
layout: home

hero:
  name: LangChain Learning Path
  text: Flat Design 学习地图
  tagline: 用纯色分块、清晰几何容器和高对比排版，把学习入口、章节主线、项目版本和支持资源压进一张没有阴影和渐变的平面信息界面。
  actions:
    - theme: brand
      text: 从新手 Setup 进入
      link: /guide/setup
    - theme: alt
      text: 查看 10 章主线
      link: /chapters/
    - theme: alt
      text: 查看项目演进
      link: /project/
---

<div class="mt-6 flex flex-col gap-6 font-sans">
  <section class="grid gap-4 lg:grid-cols-[minmax(0,1.45fr)_320px]">
    <div class="rounded-lg border border-flat-blue bg-flat-blue p-6 text-flat-surface shadow-none">
      <div class="flex flex-wrap items-start justify-between gap-4 border-b border-flat-surface pb-5">
        <div class="max-w-2xl">
          <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-surface">Flat Overview</p>
          <h2 class="mt-3 text-3xl font-bold leading-tight text-flat-surface md:text-4xl">把学习入口、章节主线和项目版本压成一张平面化学习地图。</h2>
          <p class="mt-4 max-w-2xl text-base leading-7 text-flat-muted">
            这个首页不再依赖阴影制造层次，而是用纯色分块、明确边界和大留白，让你先判断当前位置，再决定进入哪条学习路径。
          </p>
        </div>
        <div class="grid w-full max-w-[220px] gap-3 sm:w-auto">
          <div class="rounded-md border border-flat-surface bg-flat-surface p-4 text-flat-ink">
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-flat-blue">入口模式</p>
            <p class="mt-2 text-lg font-bold">Start / Core / Support</p>
          </div>
          <div class="rounded-md border border-flat-surface bg-flat-yellow p-4 text-flat-ink">
            <p class="text-xs font-bold uppercase tracking-[0.2em]">教学节奏</p>
            <p class="mt-2 text-lg font-bold">先 Setup，再章节，再项目</p>
          </div>
        </div>
      </div>
      <div class="mt-5 grid gap-4 md:grid-cols-3">
        <div class="rounded-md border border-flat-surface bg-flat-surface p-4 text-flat-ink">
          <p class="text-xs font-bold uppercase tracking-[0.2em] text-flat-blue">学习入口</p>
          <p class="mt-2 text-lg font-bold">新手 Setup / 快速开始 / 路线图</p>
        </div>
        <div class="rounded-md border border-flat-surface bg-flat-green p-4 text-flat-ink">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">章节主线</p>
          <p class="mt-2 text-lg font-bold">基础层 / 应用层 / 编排层 / 工程层</p>
        </div>
        <div class="rounded-md border border-flat-surface bg-flat-red p-4 text-flat-surface">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">项目边界</p>
          <p class="mt-2 text-lg font-bold">围绕 AI 学习助手逐章演进</p>
        </div>
      </div>
    </div>
    <aside class="rounded-lg border border-flat-line bg-flat-surface p-6 text-flat-ink shadow-none">
      <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Site Structure</p>
      <div class="mt-4 grid gap-3">
        <div class="rounded-md border border-flat-line bg-flat-muted p-4">
          <p class="text-sm font-bold">首页</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">先回答这是什么、从哪里开始。</p>
        </div>
        <div class="rounded-md border border-flat-line bg-flat-surface p-4">
          <p class="text-sm font-bold">章节目录</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">按 10 章顺序建立 LangChain 能力。</p>
        </div>
        <div class="rounded-md border border-flat-line bg-flat-muted p-4">
          <p class="text-sm font-bold">主项目</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">用同一个 AI 学习助手串起所有能力落点。</p>
        </div>
        <div class="rounded-md border border-flat-line bg-flat-surface p-4">
          <p class="text-sm font-bold">支持页</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">FAQ、术语表和故障排查集中放置。</p>
        </div>
      </div>
    </aside>
  </section>

  <section class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
    <div class="rounded-lg border border-flat-blue bg-flat-blue p-5 text-flat-surface">
      <div class="flex items-center justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Setup</p>
          <h3 class="mt-2 text-2xl font-bold">01</h3>
        </div>
        <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <path d="M12 3v18"></path>
          <path d="M3 12h18"></path>
        </svg>
      </div>
      <p class="mt-4 text-sm leading-6 text-flat-muted">先建立环境、阅读顺序和站点浏览方式。</p>
    </div>
    <div class="rounded-lg border border-flat-green bg-flat-green p-5 text-flat-ink">
      <div class="flex items-center justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Chapters</p>
          <h3 class="mt-2 text-2xl font-bold">10</h3>
        </div>
        <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <path d="M4 6h16"></path>
          <path d="M4 12h16"></path>
          <path d="M4 18h16"></path>
        </svg>
      </div>
      <p class="mt-4 text-sm leading-6 text-flat-ink">用固定主线推进，从概念到工程化逐步展开。</p>
    </div>
    <div class="rounded-lg border border-flat-red bg-flat-red p-5 text-flat-surface">
      <div class="flex items-center justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Project</p>
          <h3 class="mt-2 text-2xl font-bold">V1-V4</h3>
        </div>
        <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <path d="M5 19V5"></path>
          <path d="M12 19V9"></path>
          <path d="M19 19v-6"></path>
        </svg>
      </div>
      <p class="mt-4 text-sm leading-6 text-flat-muted">每一章都只推动一个明确能力，不切换无关 Demo。</p>
    </div>
    <div class="rounded-lg border border-flat-yellow bg-flat-yellow p-5 text-flat-ink">
      <div class="flex items-center justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Support</p>
          <h3 class="mt-2 text-2xl font-bold">FAQ</h3>
        </div>
        <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <circle cx="12" cy="12" r="9"></circle>
          <path d="M9.5 9a2.5 2.5 0 1 1 4.2 1.8c-.9.8-1.7 1.4-1.7 2.7"></path>
          <path d="M12 17h.01"></path>
        </svg>
      </div>
      <p class="mt-4 text-sm leading-6 text-flat-ink">把术语、路线图和排查建议放到统一支持区。</p>
    </div>
  </section>

  <section class="rounded-lg border border-flat-line bg-flat-surface p-6 shadow-none">
    <div class="flex flex-col gap-2 border-b border-flat-line pb-5 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Direct Navigation</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">按当前状态进入，而不是在相似卡片之间反复比较。</h2>
      </div>
      <p class="max-w-xl text-sm leading-6 text-flat-ink-soft">每个区域只使用单一纯色标题条和矩形链接块，层级由颜色、字号与留白建立。</p>
    </div>
    <div class="mt-5 grid gap-4 xl:grid-cols-3">
      <section class="rounded-lg border border-flat-line bg-flat-muted p-4">
        <div class="rounded-md bg-flat-blue px-4 py-3 text-flat-surface">
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Start Here</p>
          <h3 class="mt-2 text-xl font-bold">开始学习</h3>
        </div>
        <div class="mt-4 grid gap-3">
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/setup">
            <strong class="block text-base font-bold text-flat-ink">新手 Setup</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">先完成最小可运行环境与站点浏览。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/getting-started">
            <strong class="block text-base font-bold text-flat-ink">快速开始</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">快速理解这套学习站的阅读方式。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/study-plan">
            <strong class="block text-base font-bold text-flat-ink">学习计划</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">按 7 天、14 天、30 天节奏安排学习。</span>
          </a>
        </div>
      </section>
      <section class="rounded-lg border border-flat-line bg-flat-muted p-4">
        <div class="rounded-md bg-flat-green px-4 py-3 text-flat-ink">
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Core Paths</p>
          <h3 class="mt-2 text-xl font-bold">课程与项目</h3>
        </div>
        <div class="mt-4 grid gap-3">
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/">
            <strong class="block text-base font-bold text-flat-ink">章节目录</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">从第 1 章到第 10 章按顺序推进。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./project/">
            <strong class="block text-base font-bold text-flat-ink">主项目</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">跟着 AI 学习助手版本演进理解能力落点。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./examples/">
            <strong class="block text-base font-bold text-flat-ink">示例代码</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">查看每章对应的最小可运行示例。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./compare/">
            <strong class="block text-base font-bold text-flat-ink">方法对比</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">建立 Chain、Agent、RAG、LangGraph 的选择判断。</span>
          </a>
        </div>
      </section>
      <section class="rounded-lg border border-flat-line bg-flat-muted p-4">
        <div class="rounded-md bg-flat-orange px-4 py-3 text-flat-surface">
          <p class="text-xs font-bold uppercase tracking-[0.22em]">Support</p>
          <h3 class="mt-2 text-xl font-bold">支持与参考</h3>
        </div>
        <div class="mt-4 grid gap-3">
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/roadmap">
            <strong class="block text-base font-bold text-flat-ink">学习路线图</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">先看整体教学路径和阶段目标。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./faq/glossary">
            <strong class="block text-base font-bold text-flat-ink">术语表</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">快速回查 Runnable、Retriever、Trace 等高频术语。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./faq/">
            <strong class="block text-base font-bold text-flat-ink">FAQ</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">集中查看常见问题和排查入口。</span>
          </a>
          <a class="block rounded-md border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./faq/troubleshooting">
            <strong class="block text-base font-bold text-flat-ink">故障排查</strong>
            <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">遇到环境或构建问题时，直接查看定位建议。</span>
          </a>
        </div>
      </section>
    </div>
  </section>

  <section class="grid gap-4 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,0.8fr)]">
    <div class="rounded-lg border border-flat-line bg-flat-surface p-6 shadow-none">
      <div class="border-b border-flat-line pb-5">
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Learning Path</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">四层结构，从基础认知一路推进到工程化交付。</h2>
      </div>
      <div class="mt-5 grid gap-3">
        <div class="grid gap-3 rounded-lg border border-flat-line bg-flat-muted p-4 md:grid-cols-[64px_minmax(0,1fr)] md:items-start">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-blue text-2xl font-bold text-flat-surface">01</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">基础层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">先建立 LLM 应用视角，再理解 Prompt、Model、Parser、Runnable 和 LCEL。</p>
          </div>
        </div>
        <div class="grid gap-3 rounded-lg border border-flat-line bg-flat-muted p-4 md:grid-cols-[64px_minmax(0,1fr)] md:items-start">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-green text-2xl font-bold text-flat-ink">02</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">应用层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">从第一个链式应用开始，进入 Prompt 工程、RAG 和检索优化。</p>
          </div>
        </div>
        <div class="grid gap-3 rounded-lg border border-flat-line bg-flat-muted p-4 md:grid-cols-[64px_minmax(0,1fr)] md:items-start">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-red text-2xl font-bold text-flat-surface">03</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">编排层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">当流程变复杂时，引入 Tools、Agent 和 LangGraph，让系统可控。</p>
          </div>
        </div>
        <div class="grid gap-3 rounded-lg border border-flat-line bg-flat-muted p-4 md:grid-cols-[64px_minmax(0,1fr)] md:items-start">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-yellow text-2xl font-bold text-flat-ink">04</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">工程层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">补上评估、观测、调试和公开部署，把项目打磨成可分享作品。</p>
          </div>
        </div>
      </div>
    </div>

    <div class="rounded-lg border border-flat-ink bg-flat-ink p-6 text-flat-surface shadow-none">
      <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-yellow">Project Evolution</p>
      <h2 class="mt-2 text-3xl font-bold">AI 学习助手</h2>
      <p class="mt-4 text-sm leading-7 text-flat-muted">整个站点围绕一个持续演进的主项目。每一章只推进一个能力，不切换无关主题。</p>
      <div class="mt-5 grid gap-3">
        <div class="rounded-md border border-flat-surface bg-flat-blue p-4">
          <p class="text-sm font-bold text-flat-surface">V1</p>
          <p class="mt-2 text-sm leading-6 text-flat-muted">最小链式应用，只做主题摘要和学习顺序建议。</p>
        </div>
        <div class="rounded-md border border-flat-surface bg-flat-green p-4 text-flat-ink">
          <p class="text-sm font-bold">V2</p>
          <p class="mt-2 text-sm leading-6">通过 Prompt 工程和结构化输出，让结果更稳定。</p>
        </div>
        <div class="rounded-md border border-flat-surface bg-flat-yellow p-4 text-flat-ink">
          <p class="text-sm font-bold">V3</p>
          <p class="mt-2 text-sm leading-6">接入课程资料，升级为基础 RAG 学习助手。</p>
        </div>
        <div class="rounded-md border border-flat-surface bg-flat-red p-4">
          <p class="text-sm font-bold text-flat-surface">V4</p>
          <p class="mt-2 text-sm leading-6 text-flat-muted">引入 Tools、Agent 和 LangGraph，把系统组织成完整工作流。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="rounded-lg border border-flat-line bg-flat-surface p-6 shadow-none">
    <div class="flex flex-col gap-2 border-b border-flat-line pb-5 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Recommended Entry</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">第一次进入，直接按这三步走。</h2>
      </div>
      <p class="max-w-xl text-sm leading-6 text-flat-ink-soft">如果你已经开始做项目，再回看设计方案、课程大纲和方法对比页，建立完整判断框架。</p>
    </div>
    <div class="mt-5 grid gap-4 lg:grid-cols-[minmax(0,0.9fr)_minmax(0,1.1fr)]">
      <div class="grid gap-3">
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-muted p-4 no-underline transition-colors duration-200 hover:bg-flat-surface" href="./guide/setup">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">Step 1</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">新手 Setup</strong>
          </div>
          <span class="text-2xl font-bold text-flat-blue">01</span>
        </a>
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-muted p-4 no-underline transition-colors duration-200 hover:bg-flat-surface" href="./guide/getting-started">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-green">Step 2</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">快速开始</strong>
          </div>
          <span class="text-2xl font-bold text-flat-green">02</span>
        </a>
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-muted p-4 no-underline transition-colors duration-200 hover:bg-flat-surface" href="./guide/roadmap">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-red">Step 3</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">学习路线图</strong>
          </div>
          <span class="text-2xl font-bold text-flat-red">03</span>
        </a>
      </div>
      <div class="grid gap-3 sm:grid-cols-2">
        <a class="rounded-lg border border-flat-line bg-flat-blue p-4 text-flat-surface no-underline transition-colors duration-200 hover:bg-flat-blue-dark" href="./chapters/">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">继续阅读</p>
          <strong class="mt-3 block text-xl font-bold">章节目录</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-muted">按顺序推进完整 10 章内容。</span>
        </a>
        <a class="rounded-lg border border-flat-line bg-flat-green p-4 text-flat-ink no-underline transition-colors duration-200 hover:bg-flat-green-dark hover:text-flat-surface" href="./project/">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">继续阅读</p>
          <strong class="mt-3 block text-xl font-bold">主项目演进</strong>
          <span class="mt-2 block text-sm leading-6">跟着 AI 学习助手版本变化理解落点。</span>
        </a>
        <a class="rounded-lg border border-flat-line bg-flat-yellow p-4 text-flat-ink no-underline transition-colors duration-200 hover:bg-flat-orange" href="./DESIGN">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">背景资料</p>
          <strong class="mt-3 block text-xl font-bold">完整设计方案</strong>
          <span class="mt-2 block text-sm leading-6">理解这套教学与信息架构为何这样组织。</span>
        </a>
        <a class="rounded-lg border border-flat-line bg-flat-red p-4 text-flat-surface no-underline transition-colors duration-200 hover:bg-flat-orange-dark" href="./compare/">
          <p class="text-xs font-bold uppercase tracking-[0.2em]">选择判断</p>
          <strong class="mt-3 block text-xl font-bold">方法对比页</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-muted">先建立什么时候该选哪种方法的判断。</span>
        </a>
      </div>
    </div>
  </section>
</div>
