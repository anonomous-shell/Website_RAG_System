from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
reply exactly:

"I don't know based on the provided documents."

Do not make up information.
Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""
)