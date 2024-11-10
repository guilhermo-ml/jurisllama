# app/parsing.py

from llama_parse import LlamaParse
import os
import joblib

# Substitua com sua chave de API
LLAMA_PARSE_API_KEY = "sua_llama_parse_api_key"

# Configuração do parser
parser = LlamaParse(
    api_key=LLAMA_PARSE_API_KEY,
    result_type="markdown",
    max_timeout=5000,
    verbose=True
)

def parse_pdf(file_path):
    """Processa o PDF usando o LlamaParse e salva o resultado em formato de markdown."""
    parsed_data = parser.load_data(file_path)
    joblib.dump(parsed_data, "./data/parsed_data.pkl")
    return parsed_data

def load_or_parse_data(file_path="./data/processo_judicial.pdf"):
    """Carrega os dados processados, ou processa o PDF se não houver cache."""
    data_file = "./data/parsed_data.pkl"
    if os.path.exists(data_file):
        return joblib.load(data_file)
    return parse_pdf(file_path)
