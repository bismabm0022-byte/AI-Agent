import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Sequence
import operator

from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from tools import tools

load_dotenv()

# Define Agent State
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

# Initialize LLM & bind tools
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# Node 1: Agent Reasoning Node
def agent_node(state: AgentState):
    messages = state["messages"]
    system_prompt = SystemMessage(
        content="You are an intelligent AI Assistant capable of using tools. "
                "Always choose the appropriate tool when calculation, weather lookup, or knowledge searching is needed."
    )
    all_messages = [system_prompt] + list(messages)
    response = llm_with_tools.invoke(all_messages)
    return {"messages": [response]}

# Conditional Logic Edge
def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END

# Build LangGraph StateGraph
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
workflow.add_edge("tools", "agent")

# Compile Graph
agent_app = workflow.compile()
