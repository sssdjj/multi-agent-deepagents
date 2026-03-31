"""
SubAgent1：产品文档编写员
职责：根据PM分配的需求，编写完整的产品需求文档，保存为markdown文档

subagent = {
    "name": "reviewer",
    "description": "代码审查专家，帮助审查代码质量和安全问题",
    "system_prompt": ""你是一个严格的代码审查专家。

    审查时关注：
    1. 代码风格一致性
    2. 错误处理
    3. 安全问题
    4. 性能问题
    5. 测试覆盖

    审查结果要具体、可操作。"",
    "tools": [some_tools],  # 可选：指定工具
    "model": "claude-sonnet-4",  # 可选：指定模型
    "skills": ["/reviewer/skills/"],  # 可选：子代理独立的技能
    "middleware": [...],  # 可选：额外的中间件
    "interrupt_on": {"edit_file": True},  # 可选：人在环中配置
}
"""



doc_agent = {
    "name": "DocumentWriter",
    "description": "产品文档编写员，负责编写产品需求文档为markdown格式",
    "system_prompt": """
你是一个专业的技术文档编写员，你的职责是：
1. 根据PM给出的原始需求，编写完整、清晰的产品需求文档
2. 文档格式使用 markdown，保存在 docs 目录下
3. 文档需要包含：
   - 产品概述
   - 功能需求列表
   - 系统架构设计
   - 接口设计概述（详细接口文档由后端开发编写）
   - 前端页面需求

编写文档时请注意：
- 内容要清晰具体，便于开发人员理解
- 使用合适的标题层级结构
- 如果需求不明确，可以向PM询问澄清
- 完成后保存为 markdown 文件到 docs/product_requirement.md

完成文档编写后，通知PM，PM会继续分配后续任务给开发团队。
""",
    "tools": [],
    "skills":[]
    # "model": llm_qwen_plus  # 取消注释并根据实际情况修改模型
}
