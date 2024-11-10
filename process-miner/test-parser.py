import os
from html_parser import parse_decision_html
from storage import save_to_json, save_to_mongo

def process_directory(diretorio):
    """
    Processa todos os arquivos HTML em um diretório e salva os dados em JSON e MongoDB.
    """
    for file_name in os.listdir(diretorio):
        if file_name.endswith(".html"):
            file_path = os.path.join(diretorio, file_name)
            print(f"Processando arquivo {file_name}...")
            
            # Extrai dados e salva
            parsed_data = parse_decision_html(file_path)
            save_to_json(parsed_data)
            save_to_mongo(parsed_data)
            print(f"Dados salvos para o arquivo {file_name}.")

# Exemplo de execução
if __name__ == "__main__":
    process_directory("caminho_para_o_diretorio")
