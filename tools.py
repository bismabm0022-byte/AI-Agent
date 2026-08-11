import logging
from langchain_core.tools import tool

# Set up tool execution logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ToolLogger")

@tool
def calculate(expression: str) -> str:
    """Evaluates mathematical expressions safely. Use this for math problems, calculations, or arithmetic operations."""
    logger.info(f"🟢 [Tool Selected]: calculate | Expression: '{expression}'")
    try:
        # Simple safe evaluation for demo purposes
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expression):
            return "Error: Expression contains invalid characters."
        result = eval(expression)
        return f"Calculation Result: {result}"
    except Exception as e:
        logger.error(f"🔴 [Tool Error]: calculate failed with error: {str(e)}")
        return f"Tool Execution Error: Failed to evaluate math expression. Detail: {str(e)}"

@tool
def get_weather(city: str) -> str:
    """Gets current weather and temperature for a specified city name."""
    logger.info(f"🟢 [Tool Selected]: get_weather | City: '{city}'")
    try:
        mock_db = {
            "lahore": "Sunny, 34°C with 60% humidity.",
            "karachi": "Humid & Windy, 31°C.",
            "islamabad": "Partly Cloudy, 28°C.",
            "london": "Light Rain, 18°C.",
            "new york": "Clear Sky, 24°C."
        }
        city_clean = city.strip().lower()
        if city_clean in mock_db:
            return f"Weather in {city.title()}: {mock_db[city_clean]}"
        return f"Weather data not found for '{city}'. (Available cities: {', '.join(mock_db.keys())})"
    except Exception as e:
        logger.error(f"🔴 [Tool Error]: get_weather failed: {str(e)}")
        return f"Tool Execution Error: Could not retrieve weather. Detail: {str(e)}"

@tool
def search_knowledge_base(query: str) -> str:
    """Searches internal corporate/RAG knowledge base for rules, policies, and AI guidelines."""
    logger.info(f"🟢 [Tool Selected]: search_knowledge_base | Query: '{query}'")
    try:
        docs = {
            "python": "Python projects require PEP8 standards and type hinting across all modules.",
            "agent": "AI Agents use LLMs with a loop mechanism to call tools dynamically until task completion.",
            "langgraph": "LangGraph builds stateful, multi-actor workflows using nodes and directed cyclic graphs."
        }
        matched = [text for k, text in docs.items() if k in query.lower()]
        if matched:
            return f"Knowledge Base Results:\n" + "\n".join(f"- {m}" for m in matched)
        return f"No relevant documentation found in knowledge base for: '{query}'"
    except Exception as e:
        logger.error(f"🔴 [Tool Error]: search_knowledge_base failed: {str(e)}")
        return f"Tool Execution Error: Knowledge search failed. Detail: {str(e)}"

# Register tool list
tools = [calculate, get_weather, search_knowledge_base]
