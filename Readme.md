# 🤖 Multi-Tool AI Agent with LangGraph & LangSmith

An autonomous, multi-tool AI Agent built using **LangGraph**, **LangChain**, and **Streamlit**. The agent dynamically evaluates user input, selects and executes the appropriate tool(s), handles failures gracefully, and synthesizes a final response. Full execution tracing and evaluation are powered by **LangSmith**.

---

## ✨ Features

- **Autonomous Tool Selection:** Uses LLM function calling to decide when and which tools to trigger.
- **Custom Tool Suite:**
  - 🔢 `calculate`: Safe mathematical evaluation for arithmetic expressions.
  - 🌤️ `get_weather`: Weather lookup for supported cities.
  - 📚 `search_knowledge_base`: Internal corporate/project documentation search.
  - 🌐 `tavily_search_results_json`: Live web search integration via Tavily AI.
- **Stateful Workflow (LangGraph):** Cyclic graph setup utilizing `StateGraph` and `ToolNode` for reasoning loops.
- **Error Handling & Logging:** Detailed terminal logging for selected tools and error catching inside tool definitions.
- **Observability (LangSmith):** Automatic evaluation and step-by-step execution tracing.
- **Interactive UI (Streamlit):** Web interface displaying user chat, tool execution badges, and final responses.

---

## 🏗️ Architecture & Control Flow

```text
               +-------------------+
               |    User Input     |
               +---------+---------+
                         |
                         v
                +-----------------+
                |   Agent Node    |
                |   (LLM Decision)|
                +--------+--------+
                         |
           Does input require a tool?
                  /             \
            [Yes]               [No]
             /                     \
            v                       v
   +-----------------+      +-----------------+
   |   Tool Node     |      |   Final Answer  |
   | (Execute Tool)  |      |   (End Graph)   |
   +--------+--------+      +-----------------+
            |
            v
   (Pass observation
    back to Agent)
