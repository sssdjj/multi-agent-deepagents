from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek

tvly_key = "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"

llm_xm = ChatOpenAI(
    model="tongyi-xiaomi-analysis-pro",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="api_key"
)

llm_qwen_plus = ChatOpenAI(
    model="qwen3.5-35b-a3b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="api_key"
)

llm_deepseek = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key="sk-api_key"
)