from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import CacheBackedEmbeddings


underlying_embeddings = OpenAIEmbeddings()
store = LocalFileStore("./cache/")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)



# to create a new file named vectorstore in your current directory.
def load_db():
    embeddings=OpenAIEmbeddings()
    DB_FAISS_PATH = './.cache/faiss_index'
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization= True)
    return db
