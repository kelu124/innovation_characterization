from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import CacheBackedEmbeddings


# to create a new file named vectorstore in your current directory.
def load_db():
    store = LocalFileStore("./.cache/embeds/")
    embeddings = OpenAIEmbeddings()

    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        embeddings, store, namespace=embeddings.model
    )
    
    DB_FAISS_PATH = "./.cache/faiss_index"
    db = FAISS.load_local(
        DB_FAISS_PATH, cached_embedder, allow_dangerous_deserialization=True
    )
    return db, cached_embedder

def save_db(db):
    DB_FAISS_PATH = "./.cache/faiss_index"
    db.save_local(DB_FAISS_PATH)
    return "saved at "+DB_FAISS_PATH
