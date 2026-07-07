import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Agentic AI", page_icon="🧠", layout="wide")

st.title("🧠 Agentic AI Assistant")
st.caption("Autonomous Planning • Tool Use • Self-Correction")

# Sidebar
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    model_name = st.selectbox("Model", ["gemini-3.5-flash", "gemini-flash-latest"], index=0)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_steps = st.number_input("Max Steps", 5, 15, 8)

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Initialize LLM
def get_llm():
    if not api_key:
        return None
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        api_key=api_key
    )

llm = get_llm()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Describe your task..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Planning and executing..."):
            try:
                if not llm:
                    response = "Please enter your Gemini API Key in the sidebar."
                else:
                    # You can replace this with full agent logic later
                    full_prompt = f"You are an agentic AI. Plan and solve: {prompt}"
                    response = llm.invoke([HumanMessage(content=full_prompt)]).content
            except Exception as e:
                response = f"Error: {str(e)}"

        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
