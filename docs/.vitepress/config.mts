import { defineConfig } from "vitepress";

const repoName =
  process.env.GITHUB_REPOSITORY?.split("/")[1] || "langchain-learning-path";
const base = process.env.GITHUB_ACTIONS ? `/${repoName}/` : "/";

export default defineConfig({
  title: "LangChain Learning Path",
  description: "一个面向中文开发者的 LangChain 章节化学习站。",
  base,
  appearance: false,
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    logo: "LC",
    nav: [
      { text: "首页", link: "/" },
      {
        text: "开始学习",
        activeMatch: "^/guide/",
        items: [
          { text: "新手 Setup", link: "/guide/setup" },
          { text: "快速开始", link: "/guide/getting-started" },
          { text: "学习计划", link: "/guide/study-plan" },
          { text: "路线图", link: "/guide/roadmap" }
        ]
      },
      {
        text: "章节与项目",
        activeMatch: "^/(chapters|examples|project|compare)/",
        items: [
          { text: "章节目录", link: "/chapters/" },
          { text: "主项目", link: "/project/" },
          { text: "示例代码", link: "/examples/" },
          { text: "方法对比", link: "/compare/" }
        ]
      },
      {
        text: "支持",
        activeMatch: "^/faq/",
        items: [
          { text: "FAQ", link: "/faq/" },
          { text: "故障排查", link: "/faq/troubleshooting" },
          { text: "术语表", link: "/faq/glossary" }
        ]
      }
    ],
    sidebar: {
      "/": [
        {
          text: "LangChain Learning Path",
          items: [
            { text: "前言", link: "/" },
            { text: "从哪里开始", link: "/#从哪里开始" },
            { text: "学习主线", link: "/#学习主线" },
            { text: "继续阅读", link: "/#继续阅读" }
          ]
        }
      ],
      "/guide/": [
        {
          text: "指南",
          items: [
            { text: "新手 Setup", link: "/guide/setup" },
            { text: "快速开始", link: "/guide/getting-started" },
            { text: "学习计划", link: "/guide/study-plan" },
            { text: "学习路线图", link: "/guide/roadmap" }
          ]
        }
      ],
      "/compare/": [
        {
          text: "方法对比",
          items: [
            { text: "对比页首页", link: "/compare/" },
            { text: "LangChain vs LlamaIndex", link: "/compare/langchain-vs-llamaindex" },
            { text: "Chain vs Agent", link: "/compare/chain-vs-agent" },
            { text: "RAG vs Fine-tuning", link: "/compare/rag-vs-fine-tuning" },
            {
              text: "LangGraph vs 普通链式调用",
              link: "/compare/langgraph-vs-linear-chains"
            }
          ]
        }
      ],
      "/chapters/": [
        {
          text: "章节目录",
          items: [
            { text: "章节首页", link: "/chapters/" },
            { text: "第 1 章：LLM 应用基础", link: "/chapters/chapter-01-llm-basics" },
            { text: "第 2 章：LangChain 核心抽象", link: "/chapters/chapter-02-langchain-core" },
            { text: "第 3 章：第一个链式应用", link: "/chapters/chapter-03-first-chain" },
            { text: "第 4 章：Prompt 工程与输出控制", link: "/chapters/chapter-04-prompt-engineering" },
            { text: "第 5 章：RAG 入门", link: "/chapters/chapter-05-rag-basics" },
            { text: "第 6 章：RAG 进阶优化", link: "/chapters/chapter-06-rag-optimization" },
            { text: "第 7 章：Tools 与 Agent", link: "/chapters/chapter-07-tools-and-agents" },
            { text: "第 8 章：LangGraph 工作流", link: "/chapters/chapter-08-langgraph-workflows" },
            {
              text: "第 9 章：评估、观测与调试",
              link: "/chapters/chapter-09-evaluation-observability-debugging"
            },
            {
              text: "第 10 章：综合实战与公开部署",
              link: "/chapters/chapter-10-capstone-and-deployment"
            }
          ]
        }
      ],
      "/project/": [
        {
          text: "主项目",
          items: [{ text: "AI 学习助手", link: "/project/" }]
        }
      ],
      "/examples/": [
        {
          text: "示例代码",
          items: [{ text: "示例总览", link: "/examples/" }]
        }
      ],
      "/faq/": [
        {
          text: "帮助",
          items: [
            { text: "FAQ", link: "/faq/" },
            { text: "术语表", link: "/faq/glossary" },
            { text: "故障排查", link: "/faq/troubleshooting" }
          ]
        }
      ]
    },
    outline: {
      level: [2, 3],
      label: "本页内容"
    },
    search: {
      provider: "local"
    },
    docFooter: {
      prev: "上一页",
      next: "下一页"
    },
    returnToTopLabel: "回到顶部",
    sidebarMenuLabel: "菜单",
    darkModeSwitchLabel: "主题",
    lightModeSwitchTitle: "切换到浅色模式",
    darkModeSwitchTitle: "切换到深色模式"
  }
});
