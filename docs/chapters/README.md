# 章节目录

这里存放课程的正式章节内容。章节按“先理解应用，再建立抽象，最后完成工程化”的顺序组织，所有内容都围绕同一个主项目 `AI 学习助手` 展开。

<div class="landing-hero">
  <div class="landing-hero-copy">
    <p class="landing-kicker">Chapter Index</p>
    <h2>先看章节节奏，再决定从哪一章切入。</h2>
    <p class="landing-lead">
      这一页不是把章节散着列出来，而是把课程推进路线、章节模板和阅读入口放到同一个平面里。这样你可以先判断当前能力阶段，再进入对应章节。
    </p>
    <div class="landing-metrics">
      <div>
        <span>章节总数</span>
        <strong>10 章</strong>
      </div>
      <div>
        <span>学习主线</span>
        <strong>AI 学习助手</strong>
      </div>
      <div>
        <span>推荐节奏</span>
        <strong>按章节顺序推进</strong>
      </div>
    </div>
  </div>
  <aside class="landing-rail">
    <p class="landing-rail-label">本页用途</p>
    <ul>
      <li>先看全部章节的能力分层。</li>
      <li>再按章节定位当前阅读位置。</li>
      <li>最后回到主项目页理解版本演进。</li>
    </ul>
  </aside>
</div>

## 章节总览

<div class="landing-grid">
  <section class="landing-panel">
    <span class="landing-card-kicker">基础层</span>
    <h3>第 1 章到第 2 章</h3>
    <p>先建立 LLM 应用视角，再拆开 Prompt、Model、Parser、Runnable 和 LCEL。</p>
    <div class="landing-link-list">
      <a class="landing-link-item" href="./chapter-01-llm-basics">
        <strong>第 1 章：LLM 应用基础</strong>
        <span>先理解应用由哪些部分组成。</span>
      </a>
      <a class="landing-link-item" href="./chapter-02-langchain-core">
        <strong>第 2 章：LangChain 核心抽象</strong>
        <span>建立最小心智模型与组合方式。</span>
      </a>
    </div>
  </section>
  <section class="landing-panel">
    <span class="landing-card-kicker">应用层</span>
    <h3>第 3 章到第 6 章</h3>
    <p>把最小链式应用、Prompt 工程和 RAG 放到同一条主线上，逐步提升可用性。</p>
    <div class="landing-link-list">
      <a class="landing-link-item" href="./chapter-03-first-chain">
        <strong>第 3 章：第一个链式应用</strong>
        <span>做出 AI 学习助手 V1。</span>
      </a>
      <a class="landing-link-item" href="./chapter-04-prompt-engineering">
        <strong>第 4 章：Prompt 工程与输出控制</strong>
        <span>让输出更稳定、可消费。</span>
      </a>
      <a class="landing-link-item" href="./chapter-05-rag-basics">
        <strong>第 5 章：RAG 入门</strong>
        <span>让助手开始回答课程资料。</span>
      </a>
      <a class="landing-link-item" href="./chapter-06-rag-optimization">
        <strong>第 6 章：RAG 进阶优化</strong>
        <span>继续优化检索与回答质量。</span>
      </a>
    </div>
  </section>
  <section class="landing-panel">
    <span class="landing-card-kicker">编排层</span>
    <h3>第 7 章到第 8 章</h3>
    <p>当系统需要决策、分支和重试时，开始引入 Tools、Agent 和 LangGraph。</p>
    <div class="landing-link-list">
      <a class="landing-link-item" href="./chapter-07-tools-and-agents">
        <strong>第 7 章：Tools 与 Agent</strong>
        <span>让系统能调用外部能力。</span>
      </a>
      <a class="landing-link-item" href="./chapter-08-langgraph-workflows">
        <strong>第 8 章：LangGraph 工作流</strong>
        <span>把流程显式化，保持可控。</span>
      </a>
    </div>
  </section>
  <section class="landing-panel">
    <span class="landing-card-kicker">工程层</span>
    <h3>第 9 章到第 10 章</h3>
    <p>补上评估、观测、调试和公开部署，让项目可以真正对外展示。</p>
    <div class="landing-link-list">
      <a class="landing-link-item" href="./chapter-09-evaluation-observability-debugging">
        <strong>第 9 章：评估、观测与调试</strong>
        <span>知道怎么发现问题、比较效果。</span>
      </a>
      <a class="landing-link-item" href="./chapter-10-capstone-and-deployment">
        <strong>第 10 章：综合实战与公开部署</strong>
        <span>把项目整理成可发布作品。</span>
      </a>
    </div>
  </section>
</div>

## 统一章节结构

<div class="landing-stack">
  <div class="landing-step">
    <span class="landing-step-index">01</span>
    <div>
      <h3>章节定位</h3>
      <p>先说这一章解决什么问题，再说为什么它在主线上重要。</p>
    </div>
  </div>
  <div class="landing-step">
    <span class="landing-step-index">02</span>
    <div>
      <h3>最小示例</h3>
      <p>先给能跑的版本，再逐步加概念和约束。</p>
    </div>
  </div>
  <div class="landing-step">
    <span class="landing-step-index">03</span>
    <div>
      <h3>实践与验收</h3>
      <p>每章都要有可检查的结果，方便回看与复盘。</p>
    </div>
  </div>
</div>

## 阅读入口

<div class="landing-chip-list">
  <a href="./chapter-01-llm-basics">第 1 章</a>
  <a href="./chapter-03-first-chain">第 3 章</a>
  <a href="./chapter-05-rag-basics">第 5 章</a>
  <a href="./chapter-07-tools-and-agents">第 7 章</a>
  <a href="./chapter-10-capstone-and-deployment">第 10 章</a>
</div>

<p class="landing-note">
  移动端阅读时，建议先点开当前章节，再回到本页判断自己处于哪一层能力阶段。章节越往后，越要把前一章的输出当作当前章的输入。
</p>
