# 🌐 Website RAG Chatbot

> Chat with any website using **Retrieval-Augmented Generation (RAG)** powered by **Groq**, **Llama 3.1 8B**, **FAISS**, and **Sentence Transformers**.

---

## 📌 Overview

Website RAG Chatbot allows users to index an entire website and interact with it using natural language.

Instead of searching manually through webpages, the chatbot retrieves the most relevant information from the indexed website and generates accurate answers using an LLM.

---
 
# 🚀 Features

- 🌍 Crawl complete websites
- 📄 Extract textual content from webpages
- ✂️ Intelligent text chunking
- 🤖 Local Sentence Transformer Embeddings
- ⚡ FAISS Vector Database
- 🚀 Groq Llama 3.1 8B Integration
- 💬 Natural Language Question Answering
- 📚 Source Citation Support
- 🎨 Gradio User Interface
- 🔄 Dynamic Website Indexing

---

# 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Groq - Llama 3.1 8B |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| Framework | LangChain |
| UI | Gradio |
| Web Crawling | BeautifulSoup |
| Language | Python |

---

# 📂 Project Structure

```
Website_RAG_System/
│
├── crawler.py
├── ingest.py
├── rag.py
├── prompts.py
├── main.py
│
├── Data/
│
├── Vector_DB/
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Project Workflow

```
                 User enters Website URL
                           │
                           ▼
                    crawler.py
                           │
         Crawl Internal Website Pages
                           │
                           ▼
                     ingest.py
                           │
       Extract Text from all Web Pages
                           │
                           ▼
          Recursive Text Splitter
                           │
                           ▼
         Sentence Transformer Embeddings
                           │
                           ▼
                  FAISS Vector Store
                           │
             Saved in Vector_DB Folder
                           │
──────────────────────────────────────────────────────
                           │
                     User asks Question
                           │
                           ▼
                      rag.py
                           │
               Load FAISS Database
                           │
                           ▼
              Retrieve Relevant Chunks
                           │
                           ▼
                  Prompt Template
                           │
                           ▼
                Groq Llama 3.1 8B
                           │
                           ▼
                 Final AI Generated Answer
```

---

# 📁 Module Explanation

---

## crawler.py

### Responsibility

Discovers all internal webpages of a website.

### Workflow

```
Website URL
      │
      ▼
Visit Homepage
      │
      ▼
Extract Internal Links
      │
      ▼
Visit Every Page
      │
      ▼
Return URL List
```

---

## ingest.py

### Responsibility

Creates the Vector Database.

### Workflow

```
Website URL
      │
      ▼
Crawler
      │
      ▼
Load Web Pages
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
```

Output

```
Vector_DB/

index.faiss

index.pkl
```

---

## rag.py

### Responsibility

Handles Question Answering.

### Workflow

```
Question
    │
    ▼
Load FAISS
    │
    ▼
Retriever
    │
    ▼
Top Relevant Chunks
    │
    ▼
Prompt
    │
    ▼
Groq Llama 3.1
    │
    ▼
Answer
```

---

## prompts.py

Contains the prompt template used by the LLM.

Responsibilities

- Restrict hallucination
- Ground responses using retrieved context
- Improve answer quality

---

## main.py

Provides the Gradio Interface.

Features

- Website URL Input
- Website Indexing
- Chat Interface
- Status Updates

---

# 🧠 RAG Pipeline

```
Website
    │
    ▼
Crawler
    │
    ▼
Documents
    │
    ▼
Text Splitter
    │
    ▼
Embeddings
    │
    ▼
FAISS
    │
    ▼
Retriever
    │
    ▼
Groq LLM
    │
    ▼
Answer
```

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/anonomous-shell/Website_RAG_System.git

cd Website_RAG_System
```

Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY

LLM_MODEL=llama-3.1-8b-instant

EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

---

# ▶️ Running the Project

First create the vector database

```bash
python ingest.py
```

Enter Website URL

```
https://example.com
```

After indexing completes

Run

```bash
python main.py
```

Open

```
http://127.0.0.1:7860
```

---

# 💡 Example Workflow

```
Index Website
        │
        ▼
Create Vector Database
        │
        ▼
Ask Questions
        │
        ▼
Retrieve Relevant Context
        │
        ▼
Generate AI Response
```

---

# 📊 Architecture

```
                User
                  │
                  ▼
             Gradio UI
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Website Index        Ask Question
        │                   │
        ▼                   ▼
    ingest.py            rag.py
        │                   │
        ▼                   ▼
      FAISS           Groq LLM
        │                   │
        └─────────┬─────────┘
                  ▼
             Final Response
```

---

# 🔮 Future Improvements

- Streaming Responses
- Conversation Memory
- Multi-Website Support
- PDF + Website Hybrid RAG
- Hybrid Search (BM25 + Vector Search)
- Docker Deployment
- REST API Support
- Authentication
- Admin Dashboard

---

# 👨‍💻 Author

**Aaryansh Rathore**

GitHub

https://github.com/anonomous-shell

---

# ⭐ If you found this project useful

Give this repository a ⭐ on GitHub.
