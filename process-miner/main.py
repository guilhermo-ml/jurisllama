import os
import time
from plumber_api import iniciar_processo_r, listar_e_baixar_arquivos
from html_parser import parse_decision_html
from storage import save_to_json, save_to_mongo

def executar_fluxo(termo, diretorio, timeout=10):
    """
    Executa o fluxo completo:
    1. Inicia o processo R para download de dados.
    2. Espera o tempo determinado para o download.
    3. Baixa e processa os arquivos HTML.
    """
    print(f"Iniciando o processo com termo '{termo}' e diretório '{diretorio}'")
    
    # Etapa 1: Inicia o processo R
    status = iniciar_processo_r(termo, diretorio)
    if not status:
        print("Erro ao iniciar o processo no módulo R.")
        return
    
    # Etapa 2: Aguardar o download dos arquivos no servidor R
    print(f"Aguardando {timeout} segundos para o download dos arquivos...")
    time.sleep(timeout)

    # Etapa 3: Listar e baixar arquivos HTML do servidor R
    arquivos_baixados = listar_e_baixar_arquivos(diretorio)
    if not arquivos_baixados:
        print("Nenhum arquivo foi baixado.")
        return

    # Etapa 4: Processar arquivos HTML baixados
    for file_path in arquivos_baixados:
        print(f"Processando arquivo {file_path}...")
        
        # Extrai dados e salva
        parsed_data = parse_decision_html(file_path)
        save_to_json(parsed_data)
        save_to_mongo(parsed_data)

    print("Processo concluído com sucesso.")
