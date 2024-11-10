from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import executar_fluxo
from plumber_api import iniciar_processo_r, listar_e_baixar_arquivos
from html_parser import parse_decision_html
from storage import save_to_json, save_to_mongo

app = FastAPI()

class ProcessRequest(BaseModel):
    termo: str
    diretorio: str

@app.post("/iniciar")
async def iniciar_processo(request: ProcessRequest):
    """
    Rota para iniciar o processo de download no servidor R.
    """
    try:
        # Inicia o processo R para download de dados
        iniciar_processo_r(request.termo, request.diretorio)
        return {"status": "Processo de download iniciado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao iniciar o processo: {str(e)}")

@app.post("/processar")
async def processar_arquivos(request: ProcessRequest):
    """
    Rota para baixar os arquivos HTML do servidor R, processá-los e salvar os dados.
    """
    try:
        # Baixa os arquivos do servidor R
        arquivos_baixados = listar_e_baixar_arquivos(request.diretorio)
        if not arquivos_baixados:
            raise HTTPException(status_code=404, detail="Nenhum arquivo encontrado para processamento.")

        # Processa cada arquivo HTML baixado
        for file_path in arquivos_baixados:
            print(f"Processando arquivo {file_path}...")
            
            # Extrai dados e salva
            parsed_data = parse_decision_html(file_path)
            save_to_json(parsed_data)
            save_to_mongo(parsed_data)
            print(f"Dados salvos para o arquivo {file_path}.")

        return {"status": "Processamento concluído com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro durante o processamento: {str(e)}")
