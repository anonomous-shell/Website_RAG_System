import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser

from prompts import RAG_PROMPT

load_dotenv()

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama-3.1-8b-instant"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Create LLM only once
llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0,
)

parser = StrOutputParser()

chain = RAG_PROMPT | llm | parser


def load_retriever():
    """
    Loads the latest FAISS vector database.
    This ensures that if a new website is indexed,
    the chatbot immediately starts using the new index.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.load_local(
        "Vector_DB/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20,
        },
    )

    return retriever


def format_docs(docs):
    """Convert retrieved documents into a single context string."""
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def get_sources(docs):
    """Extract unique source URLs."""
    return list(
        {
            doc.metadata.get("source")
            for doc in docs
            if doc.metadata.get("source")
        }
    )


def ask_question(question: str):
    """
    Ask a question to the RAG pipeline.
    """

    try:
        retriever = load_retriever()
        docs = retriever.invoke(question)

    except Exception as e:
        return (
            "❌ No vector database found.\n\n"
            "Please index a website first.\n\n"
            f"Error: {str(e)}"
        )

    context = format_docs(docs)

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    sources = get_sources(docs)

    if sources:
        answer += "\n\n📚 Sources:\n"
        answer += "\n".join(
            f"• {url}"
            for url in sources
        )

    return answer