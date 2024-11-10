# app/chatbot.py

import os
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from app.templates import judicial_report_template  # Importa o novo template
from app.vector_store import create_vector_database  # Para converter o PDF em uma base vetorial

def initialize_chat_model():
    # Carrega a API Key do Groq a partir das variáveis de ambiente
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    # Inicializa o modelo de chat usando o modelo 'llama-3.1-70b' no Groq
    return ChatGroq(
        temperature=0,
        model_name="llama3-70b-8192",
        api_key=groq_api_key
    )

def create_qa_chain(vector_db, chat_model):
    try:
        # Configura o recuperador com as definições desejadas
        retriever = vector_db.as_retriever(search_kwargs={'k': 3})
        
        # Template para consultas, limitado a 'context' e 'question'
        prompt = PromptTemplate(template=judicial_report_template, input_variables=['context', 'question'])
        
        # Define a cadeia de QA com o nome correto da variável de documento
        return RetrievalQA.from_chain_type(
            llm=chat_model,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={
                "prompt": prompt
            }
        )
    except Exception as e:
        print(f"Erro ao criar a cadeia de QA: {e}")
        raise

def generate_initial_report(file_path):
    """Gera um relatório inicial do PDF processado."""
    # Carrega e processa o PDF
    parsed_data = create_vector_database(file_path)
    
    # Inicializa o modelo de chat e a cadeia de QA
    chat_model = initialize_chat_model()
    qa_chain = create_qa_chain(parsed_data, chat_model)
    
    # Gera o relatório passando 'query' como chave principal
    query = f"Contexto: {parsed_data}\nPergunta: Resumo do conteúdo"
    response = qa_chain.invoke({"query": query})
    return response['result']

def query_judicial_assistant(qa_chain, question):
    # Realiza a consulta no assistente judicial passando 'query' como chave principal
    query = f"Contexto: \nPergunta: {question}"
    response = qa_chain.invoke({"query": query})
    return response['result']
