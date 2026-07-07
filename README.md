# Agentic AI Assistant

An autonomous AI agent built with **Streamlit** and **Google Gemini**.

The agent can plan tasks, use tools, reason step-by-step, self-correct, and complete complex requests intelligently.

## Features

- Real-time streaming chat interface
- Agent reasoning transparency (see thought process)
- Tool usage (Search, Code Execution, etc.)
- Self-correction capability
- Session memory
- Easy to deploy

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: Gemini 3.5 Flash
- **Framework**: LangChain
- **Deployment**: Streamlit / Custom

## How to Run Locally

```bash
git clone https://github.com/manshiyogi13/agentic-ai-assistant.git
cd agentic-ai-assistant
pip install -r requirements.txt
streamlit run app.py
