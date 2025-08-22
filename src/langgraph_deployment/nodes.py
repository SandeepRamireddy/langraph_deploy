from .config import llm_with_tools
from .my_tools import available_tools
from langgraph.prebuilt import ToolNode


def chatbot(state):
    """Main chatbot node that invokes LLM with tools bound."""
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Tool node
tool_node = ToolNode(tools=available_tools)
