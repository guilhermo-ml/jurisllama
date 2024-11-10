# app/vector_store.py

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader
import os

def create_vector_database(parsed_data):
    os.makedirs("chroma_db_llamaparse", exist_ok=True)
    
    # Salva o texto em um arquivo markdown
    with open('./data/output.md', 'w') as f:
        for doc in parsed_data:
            f.write(doc.text + '\n')
    
    # Usa o loader de markdown para carregar o arquivo processado
    loader = UnstructuredMarkdownLoader("./data/output.md")
    documents = loader.load()
    
    # Divide o texto em chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    
    # Cria os embeddings e a base de dados vetorial
    embed_model = FastEmbedEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embed_model,
        persist_directory="chroma_db_llamaparse",
        collection_name="judicial_process"
    )
    return vector_db
