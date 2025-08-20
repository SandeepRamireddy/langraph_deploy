import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from .my_tools import available_tools

# Load environment variables
load_dotenv()

LLM_API_KEY = os.environ["LLM_API_KEY"]
LLM_API_ENDPOINT = os.environ["LLM_API_ENDPOINT"]
LLM_MODEL = os.environ["LLM_MODEL"]

# Configure LLM
llm = ChatOpenAI(
    model=LLM_MODEL,
    base_url=LLM_API_ENDPOINT,
    api_key=LLM_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# LLM with tools
llm_with_tools = llm.bind_tools(available_tools)
