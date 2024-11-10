import requests
import os

def iniciar_processo_r(termo, diretorio):
    """
    Faz uma requisição POST para a API Plumber na porta 7000 para iniciar o download de dados.
    """
    url = "http://localhost:7000/buscar"
    data = {"termo": termo, "diretorio": diretorio}
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Gera um erro para códigos de status de erro
        print(f"Resposta da API Plumber: {response.status_code} - {response.text}")
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar solicitação para API Plumber: {e}")
        return None

def listar_e_baixar_arquivos(diretorio, download_dir='downloads'):
    """
    Lista e baixa arquivos HTML do servidor R.
    """
    # Endpoint para listar os arquivos
    url_list_files = f"http://localhost:7000/listar_arquivos?diretorio={diretorio}"
    try:
        response = requests.get(url_list_files)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Erro ao listar arquivos no servidor R:", e)
        return []

    # Lista de arquivos retornada pelo servidor R
    arquivos = response.json().get("arquivos", [])
    os.makedirs(download_dir, exist_ok=True)
    
    arquivos_baixados = []
    for arquivo in arquivos:
        # Endpoint para baixar cada arquivo individualmente
        url_download = f"http://localhost:7000/download_arquivo?diretorio={diretorio}&arquivo={arquivo}"
        try:
            response = requests.get(url_download)
            response.raise_for_status()
            
            # Salva o arquivo no diretório de downloads local
            file_path = os.path.join(download_dir, arquivo)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            arquivos_baixados.append(file_path)
            print(f"Arquivo baixado: {file_path}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar o arquivo {arquivo}:", e)

    return arquivos_baixados
