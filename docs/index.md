---
layout: home

hero:
  name: LangChain Learning Path
  text: 从基础认知到 LangGraph 的清晰主线
  tagline: 把 Setup、章节、项目和支持资源放进同一套平面化入口逻辑里。先判断自己现在要解决什么，再进入对应页面，不在相似卡片之间来回比较。
  actions:
    - theme: brand
      text: 从新手 Setup 进入
      link: /guide/setup
    - theme: alt
      text: 查看章节主线
      link: /chapters/
    - theme: alt
      text: 打开学习路线图
      link: /guide/roadmap
---

<div class="mt-6 flex flex-col gap-6 font-sans">
  <section class="grid gap-4 xl:grid-cols-[minmax(0,1.25fr)_minmax(280px,0.75fr)]">
    <div class="rounded-lg border border-flat-line bg-flat-surface p-6">
      <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Start Here</p>
      <h2 class="mt-3 text-3xl font-bold leading-tight text-flat-ink md:text-4xl">先确认你处在哪个阶段，再进入对应页面。</h2>
      <p class="mt-4 max-w-3xl text-base leading-7 text-flat-ink-soft">
        首页不再强调“风格本身”，而是直接回答三件事：第一次进站从哪开始、当前主线学到哪、项目能力会落到哪里。所有主要入口统一用可点击卡片承载。
      </p>
      <div class="mt-6 grid gap-3 md:grid-cols-3">
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-blue bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/setup">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">新手入口</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">先做 Setup</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">先把环境、依赖和站点浏览方式跑通，再进入正式学习。</span>
        </a>
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-cyan bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-cyan">章节主线</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">按 10 章推进</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">从基础、应用、编排到工程化，保持同一条学习主线。</span>
        </a>
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-orange bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./project/">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-orange">项目演进</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">围绕 AI 学习助手</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">每一章只推进一个能力，不切换无关 Demo。</span>
        </a>
      </div>
    </div>

    <aside class="rounded-lg border border-flat-ink bg-flat-ink p-6 text-flat-surface">
      <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-orange">Home Logic</p>
      <h2 class="mt-3 text-2xl font-bold leading-tight">首页现在只做一件事：帮你决定下一步去哪。</h2>
      <div class="mt-5 grid gap-4">
        <div class="border-t border-flat-ink-soft pt-4">
          <p class="text-sm font-bold text-flat-surface">第一次进入</p>
          <p class="mt-2 text-sm leading-6 text-[#d8e1ea]">先看 Setup、快速开始和路线图，建立环境与学习顺序。</p>
        </div>
        <div class="border-t border-flat-ink-soft pt-4">
          <p class="text-sm font-bold text-flat-surface">已经开始学习</p>
          <p class="mt-2 text-sm leading-6 text-[#d8e1ea]">直接进入章节目录，按主线推进，不被分散页面打断。</p>
        </div>
        <div class="border-t border-flat-ink-soft pt-4">
          <p class="text-sm font-bold text-flat-surface">正在做项目</p>
          <p class="mt-2 text-sm leading-6 text-[#d8e1ea]">查看主项目、方法对比和 FAQ，补齐选择判断与排查路径。</p>
        </div>
        <div class="border-t border-flat-ink-soft pt-4">
          <p class="text-sm font-bold text-flat-surface">整站结构</p>
          <p class="mt-2 text-sm leading-6 text-[#d8e1ea]">Start、Core、Support 三层入口统一成同一种交互语言。</p>
        </div>
      </div>
    </aside>
  </section>

  <section class="rounded-lg border border-flat-line bg-flat-surface p-6">
    <div class="flex flex-col gap-2 border-b border-flat-line pb-5 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Primary Routes</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">所有主要入口都用同一种可点击卡片表达。</h2>
      </div>
      <p class="max-w-2xl text-sm leading-6 text-flat-ink-soft">这里不再混用“看起来像卡片但不能点”的块。承担跳转职责的元素统一做成整块链接，文案结构也统一为标签、标题、说明三层。</p>
    </div>

    <div class="mt-5 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-blue bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/setup">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">Start</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">新手 Setup</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">先完成最小可运行环境与站点浏览。</span>
      </a>
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-cyan bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/getting-started">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-cyan">Start</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">快速开始</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">快速理解这套学习站应该怎么读、怎么用。</span>
      </a>
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-orange bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/roadmap">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-orange">Start</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">学习路线图</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">先看整体路径和阶段目标，再决定阅读顺序。</span>
      </a>
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-blue bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">Core</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">章节目录</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">从第 1 章到第 10 章按顺序建立完整能力结构。</span>
      </a>
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-cyan bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./project/">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-cyan">Core</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">主项目演进</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">把每章能力落到同一个 AI 学习助手项目里理解。</span>
      </a>
      <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-orange bg-flat-surface p-5 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./compare/">
        <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-orange">Support</p>
        <strong class="mt-3 block text-xl font-bold text-flat-ink">方法对比</strong>
        <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">建立 Chain、Agent、RAG 和 LangGraph 的选择判断。</span>
      </a>
    </div>
  </section>

  <section class="grid gap-4 xl:grid-cols-[minmax(0,1.1fr)_minmax(0,0.9fr)]">
    <div class="rounded-lg border border-flat-line bg-flat-surface p-6">
      <div class="border-b border-flat-line pb-5">
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Learning Path</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">四层主线，直接对应四种学习目标。</h2>
      </div>
      <div class="mt-5 grid gap-3">
        <a class="grid gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-01-llm-basics">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-blue text-2xl font-bold text-flat-surface">01</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">基础层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">建立 LLM 应用视角，理解 Prompt、Model、Parser、Runnable 和 LCEL。</p>
          </div>
        </a>
        <a class="grid gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-03-first-chain">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-cyan text-2xl font-bold text-flat-surface">02</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">应用层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">从第一个链式应用开始，进入 Prompt 工程、RAG 和检索优化。</p>
          </div>
        </a>
        <a class="grid gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-07-tools-and-agents">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-orange text-2xl font-bold text-flat-surface">03</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">编排层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">当流程变复杂时，引入 Tools、Agent 和 LangGraph，让系统保持可控。</p>
          </div>
        </a>
        <a class="grid gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-09-evaluation-observability-debugging">
          <div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-ink text-2xl font-bold text-flat-surface">04</div>
          <div>
            <h3 class="text-lg font-bold text-flat-ink">工程层</h3>
            <p class="mt-2 text-sm leading-6 text-flat-ink-soft">补上评估、观测、调试和部署，把 Demo 打磨成可分享作品。</p>
          </div>
        </a>
      </div>
    </div>

    <div class="rounded-lg border border-flat-line bg-flat-surface p-6">
      <div class="border-b border-flat-line pb-5">
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-orange">Project Evolution</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">主项目的每个版本，都能对应到具体章节。</h2>
      </div>
      <div class="mt-5 grid gap-3">
        <a class="block rounded-lg border border-flat-line border-l-4 border-l-flat-blue bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-03-first-chain">
          <p class="text-sm font-bold text-flat-blue">V1</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">最小链式应用，只做主题摘要和学习顺序建议。</p>
        </a>
        <a class="block rounded-lg border border-flat-line border-l-4 border-l-flat-cyan bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-04-prompt-engineering">
          <p class="text-sm font-bold text-flat-cyan">V2</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">通过 Prompt 工程和结构化输出，让结果更稳定。</p>
        </a>
        <a class="block rounded-lg border border-flat-line border-l-4 border-l-flat-orange bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-05-rag-basics">
          <p class="text-sm font-bold text-flat-orange">V3</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">接入课程资料，升级为基础 RAG 学习助手。</p>
        </a>
        <a class="block rounded-lg border border-flat-line border-l-4 border-l-flat-ink bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-08-langgraph-workflows">
          <p class="text-sm font-bold text-flat-ink">V4</p>
          <p class="mt-2 text-sm leading-6 text-flat-ink-soft">引入 Tools、Agent 和 LangGraph，把系统组织成完整工作流。</p>
        </a>
      </div>
    </div>
  </section>

  <section class="rounded-lg border border-flat-line bg-flat-surface p-6">
    <div class="flex flex-col gap-2 border-b border-flat-line pb-5 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Recommended Sequence</p>
        <h2 class="mt-2 text-3xl font-bold text-flat-ink">第一次进入，按这个顺序最省成本。</h2>
      </div>
      <p class="max-w-2xl text-sm leading-6 text-flat-ink-soft">第一次阅读优先建立环境、理解站点结构，再进入主线。如果已经在做项目，就直接去项目页、对比页和 FAQ。</p>
    </div>

    <div class="mt-5 grid gap-4 lg:grid-cols-[minmax(0,0.88fr)_minmax(0,1.12fr)]">
      <div class="grid gap-3">
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/setup">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">Step 1</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">新手 Setup</strong>
          </div>
          <span class="flex h-12 w-12 items-center justify-center rounded-md bg-flat-blue text-xl font-bold text-flat-surface">01</span>
        </a>
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/getting-started">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-cyan">Step 2</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">快速开始</strong>
          </div>
          <span class="flex h-12 w-12 items-center justify-center rounded-md bg-flat-cyan text-xl font-bold text-flat-surface">02</span>
        </a>
        <a class="flex items-center justify-between rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./guide/roadmap">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-orange">Step 3</p>
            <strong class="mt-2 block text-lg font-bold text-flat-ink">学习路线图</strong>
          </div>
          <span class="flex h-12 w-12 items-center justify-center rounded-md bg-flat-orange text-xl font-bold text-flat-surface">03</span>
        </a>
      </div>

      <div class="grid gap-3 sm:grid-cols-2">
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-blue bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./examples/">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-blue">Support</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">示例代码</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">查看每章对应的最小可运行示例，快速对照理解。</span>
        </a>
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-cyan bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./faq/">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-cyan">Support</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">FAQ 与排查</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">遇到环境、构建和阅读路径问题时，从这里直接定位。</span>
        </a>
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-orange bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./DESIGN">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-orange">Background</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">完整设计方案</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">理解这套教学内容、导航和页面结构为何这样组织。</span>
        </a>
        <a class="block rounded-lg border border-flat-line border-t-4 border-t-flat-ink bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./faq/glossary">
          <p class="text-xs font-bold uppercase tracking-[0.18em] text-flat-ink">Reference</p>
          <strong class="mt-3 block text-xl font-bold text-flat-ink">术语表</strong>
          <span class="mt-2 block text-sm leading-6 text-flat-ink-soft">快速回查高频概念，减少在章节之间来回跳转。</span>
        </a>
      </div>
    </div>
  </section>
</div>
