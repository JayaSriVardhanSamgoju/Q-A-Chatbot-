# 🤖 Enhanced Q&A Chatbot

A multi-LLM Q&A chatbot built with **Streamlit** and **LangChain**, supporting both cloud-based (**Groq**) and local (**Ollama**) language models. Ask any question and get intelligent responses powered by state-of-the-art LLMs.

---

## ✨ Features

- 🚀 **Groq Cloud Models** — Blazing-fast inference with Llama 3.1 8B, Llama 3.3 70B, GPT OSS 120B & 20B
- 🏠 **Ollama Local Models** — Run models locally with Phi-3 Mini, Qwen 2.5 and more
- 🎛️ **Adjustable Parameters** — Control temperature and max tokens from the sidebar
- 📊 **LangSmith Tracing** — Built-in observability and debugging via LangSmith

---

## 📁 Project Structure

```
Q&A Chatbot/
├── app.py              # Groq-powered chatbot (cloud)
├── main.py             # Ollama-powered chatbot (local)
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| LLM Framework | LangChain |
| Cloud LLM | Groq API |
| Local LLM | Ollama |
| Observability | LangSmith |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed (for local models only)
- [Groq API Key](https://console.groq.com/keys) (for cloud models only)
- [LangSmith API Key](https://smith.langchain.com/) (optional, for tracing)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/qa-chatbot.git
cd qa-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
GROQ_API_KEY=your_groq_api_key
```

### 5. (Optional) Pull Ollama models

If you want to use the local chatbot, pull the models first:

```bash
ollama pull phi3:mini
ollama pull qwen2.5:7b-instruct-q4_K_M
```

### 6. Run the app

**Groq (Cloud):**
```bash
streamlit run app.py
```

**Ollama (Local):**
```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

---

## 🎮 Usage

1. Open the app in your browser
2. **For Groq** — Enter your Groq API key in the sidebar
3. Select a model from the dropdown
4. Adjust **Temperature** and **Max Tokens** as needed
5. Type your question and press Enter!

---

## 🧩 Supported Models

### Groq (Cloud) — `app.py`

| Model | Model ID | Speed |
|-------|----------|-------|
| Llama 3.1 8B | `llama-3.1-8b-instant` | 560 T/s |
| Llama 3.3 70B | `llama-3.3-70b-versatile` | 280 T/s |
| GPT OSS 120B | `openai/gpt-oss-120b` | 500 T/s |
| GPT OSS 20B | `openai/gpt-oss-20b` | 1000 T/s |

### Ollama (Local) — `main.py`

| Model | Model ID | Size |
|-------|----------|------|
| Phi-3 Mini | `phi3:mini` | 2.2 GB |
| Qwen 2.5 7B | `qwen2.5:7b-instruct-q4_K_M` | 4.7 GB |

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) — LLM application framework
- [Streamlit](https://streamlit.io/) — UI framework
- [Groq](https://groq.com/) — Fast cloud inference
- [Ollama](https://ollama.com/) — Local model serving
- [LangSmith](https://smith.langchain.com/) — LLM observability
