import gradio as gr

from ingest import build_vector_database
from rag import ask_question


def index_website(url):

    if not url.strip():
        return "⚠️ Please enter a website URL."

    try:
        total = build_vector_database(url)
        return f"✅ Successfully indexed {total} chunks."

    except Exception as e:
        return f"❌ {str(e)}"


def respond(message, history):
    return ask_question(message)


with gr.Blocks(
    title="Website RAG",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown("""
# 🌐 Website RAG

### Chat with any website using AI

**Powered by**
- 🚀 Groq
- 🦙 Llama 3.1 8B
- 📚 FAISS
- 🤗 Sentence Transformers
""")

    website = gr.Textbox(
        label="🌍 Website URL",
        placeholder="https://example.com"
    )

    button = gr.Button(
        "🚀 Index Website",
        variant="primary"
    )

    status = gr.Textbox(
        label="📋 Status",
        interactive=False
    )

    button.click(
        fn=index_website,
        inputs=website,
        outputs=status
    )

    gr.ChatInterface(
        fn=respond,
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(
            placeholder="Ask anything about the indexed website..."
        )
    )

    gr.Markdown(
        """
---
<div align="center">

### 👨‍💻 Created by <b>Aaryansh Rathore</b>

⭐ <a href="https://github.com/anonomous-shell" target="_blank">
GitHub Profile
</a>

</div>
"""
    )

if __name__ == "__main__":
    demo.launch()