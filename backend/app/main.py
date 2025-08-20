from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from langgraph_deployment.agent import get_agent
from langchain_core.messages import AIMessageChunk
from sse_starlette import EventSourceResponse
from langfuse.langchain import CallbackHandler
from contextlib import asynccontextmanager
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from app.models import ChatInput
from app.tracing import configure_tracing
from langgraph.checkpoint.memory import InMemorySaver
import time


load_dotenv()


handlers = {}
agents = {}
db_connection = {}
checkpointers = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    handlers["langfuse"] = CallbackHandler()
    checkpointers["memory"] = InMemorySaver()
    agents["calculator"] = get_agent(checkpointer=checkpointers["memory"])
    configure_tracing(__name__)
    yield
    del checkpointers["memory"]
    del handlers["langfuse"]
    del agents["calculator"]


app = FastAPI(lifespan=lifespan)

FastAPIInstrumentor.instrument_app(app)


@app.post("/agent/{agent}")
async def invoke_agent(agent: str, chat_input: ChatInput):
    session_id = chat_input.session_id
    resp = await agents[agent].ainvoke(
        chat_input.dict(),
        config={
            "callbacks": [handlers["langfuse"]],
            "configurable": {"thread_id": session_id},
        },
    )
    return resp["messages"][-1].content


async def stream_generator(agent, chat_input: dict):
    async for msg, metadata in agent.astream(
        chat_input, stream_mode="messages", config={"callbacks": [handlers["langfuse"]]}
    ):
        if isinstance(msg, AIMessageChunk) and msg.content:
            yield msg


@app.post("/agent/stream/{agent}")
async def stream_agent(agent: str, chat_input: ChatInput):
    return EventSourceResponse(stream_generator(agents[agent], chat_input.dict()))
