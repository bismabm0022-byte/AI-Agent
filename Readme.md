## Core Concepts Breakdown
 ## Tool Calling vs. Function CallingFunction Calling:
 A capability offered by LLM provider APIs (OpenAI, Anthropic, Gemini, Groq) where you provide JSON schemas of functions, and the model outputs structured JSON indicating which function to run and with what arguments.
 Tool Calling: A higher-level abstraction in frameworks like LangChain/LangGraph that wraps Python functions into standardized Tool objects. It handles schema generation, input validation, execution, and output formatting automatically.
 LLM Call vs. AI Agent
 FeatureNormal LLM CallAI Agent (e.g., LangGraph ReAct)ExecutionSingle-pass request and response (input $\rightarrow$ text output).
 Continuous loop: Reason $\rightarrow$ Act $\rightarrow$ Observe $\rightarrow$ Repeat.Tool UsageReturns intent/JSON asking you to run a tool, but cannot run it itself.Decides whether to use tools, calls them autonomously, receives results, and keeps reasoning.Control FlowRigid, single turn.Dynamic, multi-step orchestration (via state graphs).
 Project Architecture (LangGraph + LangSmith + Streamlit)Here is the complete codebase satisfying all core requirements and bonus criteria:At least 2 Custom Tools: Calculator + Weather + Custom Python RAG / KB tool.
 ## LangGraph Workflow: 
 Custom state graph with StateGraph and ToolNode.  LangSmith Tracing: Automatic execution tracking and debugging.  Error Handling & Logging: Robust exceptions inside tools and custom logger output.  File StructurePlaintextai-agent-tool-calling/
│
├── .env
├── requirements.txt
├── tools.py
├── agent.py
└── app.py
