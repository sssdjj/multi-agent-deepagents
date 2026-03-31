import os
import sys
from pathlib import Path
from typing import Any

from deepagents import create_deep_agent
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from deepagents.backends import LocalShellBackend

from models import llm_deepseek
from react_agent import (
    backend_agent,
    devops_agent,
    doc_agent,
    frontend_agent,
    review_agent,
    test_agent,
)

# Load environment variables from .env file
load_dotenv()

# System prompt for Product Manager agent
SYSTEM_PROMPT = """
你是一个经验丰富的产品经理PM，你负责：
1. 分析用户的原始需求
2. 将需求拆解为清晰的开发任务
3. 将任务分配给对应的子Agent去执行
4. 协调各个子Agent之间的工作流程
5. 确保项目按照正确的顺序推进

当前项目的分工如下：
- DocumentWriter（产品文档编写员）：根据需求书写产品文档，沉淀为 markdown 格式
- BackendDeveloper（后端开发工程师）：根据产品文档开发 Python 后端代码，并编写接口文档
- FrontendDeveloper（前端开发工程师）：根据产品文档和后端接口说明，开发 HTML + JS 前端代码
- CodeReviewer（测试架构师）：review 后端和前端代码，检查问题并让对应agent修改，检查项目完整性，输出测试用例
- DevOps（运维工程师）：负责将项目在本机部署运行
- Tester（测试工程师）：根据测试用例执行测试，验证项目功能

你的工作流程：
1. 接收用户的原始需求
2. 整理需求，将需求传递给 DocumentWriter 编写产品文档
3. 产品文档完成后，传递给 BackendDeveloper 开发后端，同时传递给 FrontendDeveloper 开发前端
4. 开发完成后，通知 CodeReviewer 进行代码评审和生成测试用例
5. 代码评审完成后，通知 DevOps 进行部署
6. 部署完成后，通知 Tester 执行测试
7. 测试完成后，向用户汇报最终结果

你需要始终保持项目按流程推进，每个步骤完成后再进入下一步。
如果某个环节出现问题，你需要协调解决后再继续。
"""


def main():
    llm = llm_deepseek
    checkpointer = MemorySaver()

    # Project root directory (current script directory)
    root_dir = str(Path(__file__).parent.resolve()).replace("\\", "/")
    print(f"Project root: {root_dir}")

    # Skills root path (points to skills directory)
    skill_root = f"{root_dir}/skills"

    # Current virtualenv Python interpreter path
    python_exec = sys.executable

    # Initialize LocalShellBackend
    backend = LocalShellBackend(
        root_dir=root_dir,
        # Pass environment variables including custom core variables
        env={
            **os.environ.copy(),
            "PYTHONHASHSEED": "0",
            "SKILL_ROOT": skill_root,
            "PYTHON_EXEC": python_exec,
        },
        timeout=120,
        max_output_bytes=100000,
        virtual_mode=True
    )

    # Configure all subagents
    doc_agent["model"] = llm
    doc_agent["skills"] = [skill_root]
    backend_agent["model"] = llm
    frontend_agent["model"] = llm
    review_agent["model"] = llm
    devops_agent["model"] = llm
    test_agent["model"] = llm

    subagents = [backend_agent, devops_agent, doc_agent, frontend_agent, review_agent, test_agent]

    # Create the deep agent
    agent = create_deep_agent(
        model=llm,
        backend=backend,
        subagents=subagents,
        checkpointer=checkpointer,
        system_prompt=SYSTEM_PROMPT,
        memory=["AGENTS.md"]
    )
    agent.get_graph().draw_mermaid()

    # Interactive loop
    print("===== 智能助手已启动，输入 q 退出 =====")
    while True:
        try:
            question = input("\n请输入需求: ").strip()
            if not question:
                continue
            if question.lower() == "q":
                print("===== 智能助手已退出 =====")
                break

            for chunk_type, chunk in agent.stream(
                {"messages": [{"role": "user", "content": question}]},
                config={"configurable": {"thread_id": "multi-agent-dev"}},
                stream_mode=["updates"]
            ):
                if "SkillsMiddleware.before_agent" in chunk and chunk["SkillsMiddleware.before_agent"]:
                    skills = chunk["SkillsMiddleware.before_agent"]["skills_metadata"]
                    print("\n" + ">" * 10 + " 加载Skills " + "<" * 30)
                    for skill in skills:
                        print(f"Load Skill: {skill['name']}")
                    # Add blank line after skills
                    print()

                # Output AI message content
                if "model" in chunk:
                    message = chunk["model"]["messages"][0]
                    if message.content:
                        print("\n" + ">" * 10 + "  AIMessage  " + "<" * 30)
                        print(message.content)
                        print()

                    # Output tool calls information
                    tool_calls = message.tool_calls
                    if tool_calls:
                        print("\n" + ">" * 10 + "  Call Tools  " + "<" * 30)
                        for t in tool_calls:
                            print(f"Tool: {t['name']} , Args: {t['args']}")
                        print()

                # Output tool execution results
                if "tools" in chunk:
                    print("\n" + ">" * 20 + "  Tools Output  " + "<" * 20)
                    for m in chunk["tools"]["messages"]:
                        print(f"Tool: {m.name}\nOutput:\n{m.content}\n")

        except KeyboardInterrupt:
            print("\n\n===== 智能助手已退出 =====")
            break
        except Exception as e:
            print(f"\n[ERROR] {e}")
            continue


if __name__ == "__main__":
    main()