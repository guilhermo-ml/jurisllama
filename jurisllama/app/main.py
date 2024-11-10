from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient  # Conectar ao MongoDB
from app.parsing import load_or_parse_data
from app.vector_store import create_vector_database
from app.chatbot import initialize_chat_model, create_qa_chain, query_judicial_assistant
import os
import nltk

# Configurações do MongoDB
MONGO_HOST = "localhost"
MONGO_PORT = 27017
DATABASE_NAME = "decisoes_tjsp"
COLLECTION_NAME = "primeiro_grau"

# Conecta ao MongoDB
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Configura o caminho do nltk_data para resolver o LookupError
nltk.data.path.append("/home/algoritme/Documentos/projetos/llama-impact/jurisllama-0001/nltk_data")

app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    os.makedirs("./data", exist_ok=True)
    
    file_name = file.filename or "arquivo_padrao.pdf"
    file_path = os.path.join("./data", file_name)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    parsed_data = load_or_parse_data(file_path)
    vector_db = create_vector_database(parsed_data)
    
    return {"message": "PDF processado com sucesso"}

@app.get("/analisar_pedidos/")
async def analisar_pedidos():
    try:
        vector_db = create_vector_database(load_or_parse_data())
        chat_model = initialize_chat_model()
        qa_chain = create_qa_chain(vector_db, chat_model)
        
        prompt = "Identifique todos os pedidos feitos pela parte autora no processo."
        result = query_judicial_assistant(qa_chain, prompt)
        
        return {"pedidos": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
async def judicial_query(request: QueryRequest):
    try:
        chat_model = initialize_chat_model()
        vector_db = create_vector_database(load_or_parse_data())
        qa_chain = create_qa_chain(vector_db, chat_model)
        result = query_judicial_assistant(qa_chain, request.question)
        return {"answer": result}
    except Exception as e:
        print(f"Erro interno: {e}")
        raise HTTPException(status_code=500, detail="Erro interno no servidor.")

@app.post("/search-decisions/")
async def search_decisions(request: QueryRequest):
    try:
        search_term = request.question.split("sobre")[-1].strip()
        results = collection.find({"teor_decisao": {"$regex": search_term, "$options": "i"}})
        
        decisions = [
            {
                "processo": result.get("processo"),
                "teor_decisao": result.get("teor_decisao")[:500],  # Limita a pré-visualização
                "link": f"http://localhost:8111/view-decision/{result.get('processo')}"  # Link interno para visualização completa
            }
            for result in results
        ]
        
        return {"decisions": decisions}  # Sempre retorna um array, mesmo se vazio
    except Exception as e:
        print(f"Erro interno na pesquisa: {e}")
        raise HTTPException(status_code=500, detail="Erro na busca de decisões.")



@app.get("/view-decision/{processo_id}")
async def view_decision(processo_id: str):
    """Endpoint para recuperar o conteúdo completo de uma decisão com base no número do processo"""
    try:
        # Busca no MongoDB pelo processo específico
        decision = collection.find_one({"processo": processo_id})
        if not decision:
            return {"detail": "Processo não encontrado."}

        # Retorna o conteúdo completo do processo
        return {
            "processo": decision.get("processo"),
            "teor_decisao": decision.get("teor_decisao")
        }
    except Exception as e:
        print(f"Erro ao buscar o processo {processo_id}: {e}")
        raise HTTPException(status_code=500, detail="Erro ao buscar a decisão.")
