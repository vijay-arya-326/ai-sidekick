import os
import sqlite3
from os import system
from typing import Annotated, TypedDict
from dotenv import load_dotenv
import gradio as gr

from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.constants import START
from langgraph.graph import add_messages, StateGraph
from datetime import datetime
from langgraph.prebuilt import ToolNode, tools_condition
from tools.folderTools import create_folder_tool
load_dotenv(override=True, dotenv_path="dev.env")
from tools.validate_required_keys import validate_required_keys
validate_required_keys()

## TOOLS IMPORT
from tools.sendHtmlMail import sendGridApiKey, sendHtmlEmailTool
from tools.webSearchTool import webSearchTool
from tools.replTool import python_repl
from tools.wikiWrapperTool import wiki_tool
from tools.FileManagement import fileToolKit, fileTools
from tools.runShellCommand import runCommand, runCommandTool

memory = MemorySaver()

db_path = "memory/memory.db"
conn = sqlite3.connect(db_path, check_same_thread=False)
sql_memory = SqliteSaver(conn)

memoryConfig = {"configurable": {"thread_id": "personal-assistant-1"}}
print(runCommandTool.invoke("pwd"))

class State(TypedDict):
    messages: Annotated[list, add_messages]
chatModel = os.getenv("GPT_MODEL")
chatAgent = ChatOpenAI(model=chatModel)
tools = [sendHtmlEmailTool, webSearchTool, python_repl, runCommandTool]
tools.append(create_folder_tool)
tools +=  fileTools
chatAgentWithTools = chatAgent.bind_tools(tools)

gb = StateGraph(State)


def AgentChat(state: State):
    return {"messages": [chatAgentWithTools.invoke(state['messages'])]}

gb.add_node("agentChat", AgentChat)
gb.add_node("tools", ToolNode(tools=tools))

gb.add_conditional_edges("agentChat", tools_condition, "tools")
gb.add_edge(START, "agentChat")

g = gb.compile(checkpointer= sql_memory)

def chatWithMe(userInput: str, history):
    result = g.invoke({"messages": [{"role": "user", "content": userInput}]}, memoryConfig)
    return result["messages"][-1].content

gr.ChatInterface(chatWithMe).launch(server_name="0.0.0.0",server_port=7860)