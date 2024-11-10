import os
import json
from pymongo import MongoClient

def save_to_json(data, output_dir='output_json'):
    """
    Salva os dados em um arquivo JSON dentro do diretório especificado.
    Se o diretório não existir, ele será criado.
    """
    # Cria o diretório se ele não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define o nome do arquivo JSON, usando um identificador padrão se 'processo' for None
    file_name = f"{data.get('processo', 'processo_desconhecido')}.json"
    file_path = os.path.join(output_dir, file_name)
    
    # Salva os dados em JSON
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Dados salvos em JSON: {file_path}")

def save_to_mongo(data):
    """
    Salva os dados no MongoDB. Se um documento com o mesmo número de processo já existir,
    ele será atualizado. Caso contrário, um novo documento será inserido.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client['decisoes_tjsp']
    collection = db['primeiro_grau']
    
    # Verifica se o processo já existe na coleção
    existing_document = collection.find_one({"processo": data["processo"]})
    
    if existing_document:
        # Atualiza o documento existente com novos dados
        result = collection.update_one(
            {"processo": data["processo"]},
            {"$set": data}
        )
        print(f"Dados atualizados no MongoDB para o processo {data['processo']}.")
    else:
        # Insere um novo documento se o processo não existir
        result = collection.insert_one(data)
        print(f"Novo documento inserido no MongoDB com o ID: {result.inserted_id}")
