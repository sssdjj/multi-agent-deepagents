import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek


load_dotenv()
# LLM configurations - API keys are loaded from environment variables
# Copy .env to .env and fill in your API keys

print(os.getenv("DASHSCOPE_API_KEY"))
# 通义千问 - 阿里云 dashscope
llm_xm = ChatOpenAI(
    model="tongyi-xiaomi-analysis-pro",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

llm_qwen_plus = ChatOpenAI(
    model="qwen3.5-35b-a3b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

# DeepSeek
llm_deepseek = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
