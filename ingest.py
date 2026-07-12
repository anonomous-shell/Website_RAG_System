import os

from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from crawler import crawl_website

load_dotenv()


def build_vector_database(website: str):
    """
    Crawl the website, create embeddings and store them in FAISS.
    """

    embedding_model = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )

    print(f"\n🌐 Crawling: {website}")

    urls = crawl_website(
        website,
        max_pages=50,
    )

    print(f"✅ Found {len(urls)} pages")

    documents = []

    for index, url in enumerate(urls, start=1):

        print(f"[{index}/{len(urls)}] Loading: {url}")

        try:

            loader = WebBaseLoader(url)

            docs = loader.load()

            documents.extend(docs)

        except Exception as e:

            print(f"❌ Failed: {url}")
            print(e)

    print(f"\n✅ Downloaded {len(documents)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=embedding_model
    )

    print("Creating FAISS Index...")

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    os.makedirs(
        "Vector_DB",
        exist_ok=True,
    )

    vectorstore.save_local(
        "Vector_DB/faiss_index"
    )

    print("✅ FAISS Index Saved Successfully")

    return len(chunks)


if __name__ == "__main__":

    website = input("Enter Website URL: ").strip()

    total_chunks = build_vector_database(website)

    print(f"\n🎉 Indexed {total_chunks} chunks successfully.")