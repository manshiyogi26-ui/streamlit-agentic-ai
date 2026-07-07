import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Agentic AI", page_icon="🧠", layout="centered")

st.title("🧠 Agentic AI Assistant")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Gemini API Key", type="password")
    model = st.selectbox("Model", ["gemini-3.5-flash", "gemini-flash-latest"])
    if st.button("Clear Chat"):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me to do anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Agent is working..."):
            try:
                llm = ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=0.7)
                response = llm.invoke([HumanMessage(content=prompt)])
                answer = response.content
            except Exception as e:
                answer = f"Error: {str(e)}"
            
            st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
