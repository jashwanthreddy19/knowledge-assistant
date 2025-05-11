# 📚 Knowledge Assistant (Streamlit + LangChain)

An intelligent, modular knowledge assistant built using:
- **LangChain agents & tools**
- **HuggingFace or OpenAI-compatible models**
- **Streamlit UI for user interaction**
- **Document ingestion + vector search for Retrieval-Augmented Generation (RAG)**

---

## 🚀 Features

- ✅ Calculator tool for math expressions  
- ✅ RAG pipeline for answering from local documents  
- ✅ Support for HuggingFace-hosted models or OpenAI-compatible APIs  
- ✅ Modular tool setup with LangChain agents  
- ✅ Simple frontend via Streamlit  

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/knowledge-assistant.git
cd knowledge-assistant
```
2. Create a Python Virtual Environment
```bash
python -m venv venv
```
Activate the environment:

On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
3. Install Required Packages
```bash
pip install -r requirements.txt
```
🔐 Setup .env File
Create a .env file in the root of your project and add the necessary keys:

env
# Example .env file

# HuggingFace API key (required for HuggingFaceEndpoint)
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here

# OpenAI-style API (optional, if using ChatOpenAI agent)
OPENAI_API_KEY=your_openai_key_here
OPENAI_API_BASE=https://api.aimlapi.com/v1
⚠️ Note: You must request access to use gated models like Gemma or Llama.

📄 Add Your Documents
Place your .txt files in the docs/ directory. These will be loaded, chunked, and indexed when the app runs.

💡 Running the App
```bash
streamlit run src/app.py
```
After starting, open your browser and visit:
```bash
http://localhost:8501
```
⚙️ Folder Structure
```bash
knowledge-assistant/
│
├── docs/                   # Your input text documents
├── logs/                   # Log files
├── src/
│   ├── app.py              # Streamlit frontend
│   ├── agent.py            # LangChain agent logic
│   ├── ingest.py           # Loads and splits docs
│   ├── embed_index.py      # Builds FAISS index
│   ├── llm.py              # LLM wrapper (calls HuggingFace/OpenAI)
│   ├── tools.py            # Tools: Calculator & RAG
│   └── logger.py           # Logging setup
│
├── .env                    # API keys (not committed)
├── requirements.txt
└── README.md
```
✨ Sample Query Examples
Math:

What is 23 * (45 + 17)?
→ Uses the Calculator tool.

Knowledge:

Who is Virat Kohli?
→ Retrieves and summarizes from virat.txt.
