# 🗄️ FinSolve Role-Based AI Chatbot

**FinSolve Role-Based Chatbot** is a secure, AI-powered internal chatbot built for FinTech companies. It allows authenticated users to query role-specific information using natural language, powered by RAG (Retrieve, Augment, Generate) architecture and modern LLMs.

---

## 🚀 Features

- 🔐 Role-Based Access Control (RBAC)
- 🤖 LLM-Powered Q&A with context-rich responses
- 🧠 RAG pipeline using ChromaDB + Google Embeddings + Groq
- 👨‍💼 Admin Panel to add/delete users and assign roles
- 🖼️ Beautiful Streamlit-based UI
- 💾 Persistent Chroma Vector DB

---

## ⚙️ Tech Stack

| Component       | Tool                     |
|-----------------|--------------------------|
| Backend         | FastAPI, Streamlit       |
| LLM             | LLaMA3 (via Groq API)    |
| Embeddings      | GoogleGenerativeAI       |
| Vector Store    | ChromaDB (Persistent)    |
| Auth & Roles    | SQLite + RBAC Logic      |
| UI              | Streamlit                |

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/codebasics/ds-rpc-01.git
cd ds-rpc-01

### 2. Create Virtual Environment & Install Dependencies

``` bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3.Add Environment Variables
- ADMIN_USERNAME=admin
- ADMIN_PASSWORD=admin123
- GOOGLE_API_KEY=your_google_api_key
- =your_groq_api_key

### 4.📄 HR Data Conversion
- Just run the csv_to_md notebook for conversion of HR CSV files into markdown format.
- The generated .md files should be placed inside the data/hr/ folder.

### 5.▶️ Run the App
-  Open the terminal and run 'streamlit run streamlit_app.py'

