---
layout: home

hero:
  name: LangChain Learning Path
  text: 从基础到 LangGraph
---

<div class="mt-6 flex flex-col gap-6 font-sans">
<section class="grid gap-3 md:grid-cols-3">
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
</section>

<section class="grid gap-4 xl:grid-cols-2">
<div class="rounded-lg border border-flat-line bg-flat-surface p-6">
<div class="border-b border-flat-line pb-5">
<p class="text-xs font-bold uppercase tracking-[0.24em] text-flat-blue">Learning Path</p>
<h2 class="mt-2 text-3xl font-bold text-flat-ink">四层主线，直接对应四种学习目标。</h2>
</div>
<div class="mt-5 grid gap-3">
<a class="grid min-h-[108px] gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-01-llm-basics">
<div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-blue text-2xl font-bold text-flat-surface">01</div>
<div>
<h3 class="text-lg font-bold text-flat-ink">基础层</h3>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">建立 LLM 应用视角，理解 Prompt、Model、Parser、Runnable 和 LCEL。</p>
</div>
</a>
<a class="grid min-h-[108px] gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-03-first-chain">
<div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-cyan text-2xl font-bold text-flat-surface">02</div>
<div>
<h3 class="text-lg font-bold text-flat-ink">应用层</h3>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">从第一个链式应用开始，进入 Prompt 工程、RAG 和检索优化。</p>
</div>
</a>
<a class="grid min-h-[108px] gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-07-tools-and-agents">
<div class="flex h-16 w-16 items-center justify-center rounded-md bg-flat-orange text-2xl font-bold text-flat-surface">03</div>
<div>
<h3 class="text-lg font-bold text-flat-ink">编排层</h3>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">当流程变复杂时，引入 Tools、Agent 和 LangGraph，让系统保持可控。</p>
</div>
</a>
<a class="grid min-h-[108px] gap-3 rounded-lg border border-flat-line bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted md:grid-cols-[64px_minmax(0,1fr)] md:items-start" href="./chapters/chapter-09-evaluation-observability-debugging">
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
<a class="flex min-h-[108px] flex-col justify-center rounded-lg border border-flat-line border-l-4 border-l-flat-blue bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-03-first-chain">
<p class="text-sm font-bold text-flat-blue">V1</p>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">最小链式应用，只做主题摘要和学习顺序建议。</p>
</a>
<a class="flex min-h-[108px] flex-col justify-center rounded-lg border border-flat-line border-l-4 border-l-flat-cyan bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-04-prompt-engineering">
<p class="text-sm font-bold text-flat-cyan">V2</p>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">通过 Prompt 工程和结构化输出，让结果更稳定。</p>
</a>
<a class="flex min-h-[108px] flex-col justify-center rounded-lg border border-flat-line border-l-4 border-l-flat-orange bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-05-rag-basics">
<p class="text-sm font-bold text-flat-orange">V3</p>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">接入课程资料，升级为基础 RAG 学习助手。</p>
</a>
<a class="flex min-h-[108px] flex-col justify-center rounded-lg border border-flat-line border-l-4 border-l-flat-ink bg-flat-surface p-4 no-underline transition-colors duration-200 hover:bg-flat-muted" href="./chapters/chapter-08-langgraph-workflows">
<p class="text-sm font-bold text-flat-ink">V4</p>
<p class="mt-2 text-sm leading-6 text-flat-ink-soft">引入 Tools、Agent 和 LangGraph，把系统组织成完整工作流。</p>
</a>
</div>
</div>
</section>
</div>
