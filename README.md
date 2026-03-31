# Multi-Agent DeepAgents

基于 [deepagents](https://github.com/...) 框架开发的多智能体协作开发系统，实现了产品开发全流程的AI多角色协作。

## 🤖 智能角色

项目定义了 **7 个不同角色** 的 AI 智能代理协同工作：

| 角色 | 职责 |
|------|------|
| **ProductManager** (PM) | 产品经理 - 分析用户需求、拆解任务、协调开发流程 |
| **DocumentWriter** | 文档编写员 - 编写完整的产品需求文档 |
| **BackendDeveloper** | 后端开发工程师 - 开发 Python 后端代码和接口文档 |
| **FrontendDeveloper** | 前端开发工程师 - 开发 HTML/JS 前端代码 |
| **CodeReviewer** | 代码评审员 - 检查代码质量、生成测试用例 |
| **DevOps** | 运维工程师 - 在本机部署项目确保可运行 |
| **Tester** | 测试工程师 - 执行测试用例，输出测试报告 |

## 🚀 快速开始

### 1. 环境要求

- Python 3.10+
- DeepAgents 框架

### 2. 安装依赖

```bash
git clone https://github.com/sssdjj/multi-agent-deepagents.git
cd multi-agent-deepagents
pip install -r requirements.txt
```

### 3. 配置 API Key

复制环境变量示例文件：

```bash
cp .env .env
```

编辑 `.env` 文件，填入你的 API Key：

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 4. 运行

```bash
python skill_tools_subagents.py
```

## 📋 工作流程

1. **需求输入** - 用户输入原始开发需求
2. **需求分析** - PM 整理分析需求
3. **文档编写** - DocumentWriter 编写产品需求文档
4. **并行开发** - BackendDeveloper + FrontendDeveloper 同时开发
5. **代码评审** - CodeReviewer 检查代码质量并生成测试用例
6. **部署** - DevOps 在本地部署项目
7. **测试** - Tester 执行测试用例输出报告
8. **交付** - PM 向用户汇报最终结果

整个过程**完全自动化**，AI 团队会按照流程一步一步完成你的开发需求。

## 📁 项目结构

```
multi-agent-deepagents/
├── models.py                 # LLM 模型配置
├── skill_tools_subagents.py  # 主入口文件
├── requirements.txt          # 项目依赖
├── pyproject.toml           # 项目配置
├── .env.example             # 环境变量示例
├── .gitignore               # Git 忽略规则
├── react_agent/             # 各个角色的智能代理定义
│   ├── __init__.py
│   ├── backend_agent.py     # 后端开发代理
│   ├── devops_agent.py      # DevOps 代理
│   ├── doc_agent.py         # 文档编写代理
│   ├── frontend_agent.py    # 前端开发代理
│   ├── review_agent.py      # 代码评审代理
│   └── test_agent.py        # 测试代理
└── skills/                  # Skills 目录
```

## ⚙️ 配置说明

项目支持多种 LLM 配置，在 `models.py` 中可以选择：

- **DeepSeek** - 默认推荐
- **通义千问** - 阿里云 Dashscope

只需要在 `.env` 中配置对应的 API Key 即可。

## 📝 示例

启动后直接输入你的开发需求，例如：

> "帮我开发一个待办事项Todo List Web应用，使用FastAPI后端+HTML前端"

AI 团队会自动按照流程完成：产品文档 → 后端开发 → 前端开发 → 代码评审 → 部署 → 测试。

## 🎯 项目目标

这是一个演示项目，展示了如何使用 deepagents 框架构建多智能体协作开发系统。适合学习：

- 多智能体协作模式
- deepagents 框架使用
- LangGraph 基础概念
- AI 辅助软件开发

## 📄 许可证

MIT License

## 🙏 致谢

- [deepagents](https://github.com/deep-ai-agents/deepagents) - 强大的AI多代理框架
