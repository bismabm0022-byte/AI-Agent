import streamlit as st
from langchain_core.messages import HumanMessage, ToolMessage
from agent import agent_app

st.set_page_config(page_title="AI Tool-Calling Agent", page_icon="🤖")

st.title("🤖 Multi-Tool AI Agent (LangGraph)")
st.write("Demonstrating autonomous tool selection, execution, and response synthesis.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Ask a question (e.g., 'What is 154 * 23?' or 'Weather in Karachi?')")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Agent is reasoning and checking tools..."):
            inputs = {"messages": [HumanMessage(content=user_input)]}
            output = agent_app.invoke(inputs)
            
            # Highlight tool calls in UI
            for msg in output["messages"]:
                if isinstance(msg, ToolMessage):
                    st.info(f"🛠️ **Tool Used ({msg.name}):** `{msg.content}`")

            final_response = output["messages"][-1].content
            st.markdown(final_response)
            
            st.session_state.messages.append({"role": "assistant", "content": final_response})
