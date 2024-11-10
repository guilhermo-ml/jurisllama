from bs4 import BeautifulSoup
import re

def parse_decision_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Dicionário para armazenar os dados extraídos
    decision_data = {}

    # Extrair o número do processo usando padrões
    processo = None
    processo_tag = soup.find('span', class_='fonteNegrito')
    if processo_tag:
        processo = processo_tag.get_text(strip=True)
    else:
        processo_tag = soup.find(text="Processo Digital nº:") or soup.find(text="Processo nº:")
        if processo_tag:
            processo = processo_tag.find_next().get_text(strip=True)
    decision_data['processo'] = processo

    # Dicionário de rótulos para os campos essenciais
    labels = {
        "Classe:": "classe",
        "Assunto:": "assunto",
        "Magistrado:": "magistrado"
    }

    # Extração dos campos essenciais com base nos rótulos
    for label, key in labels.items():
        field = soup.find('strong', text=label)
        if field:
            sibling = field.find_next_sibling(text=True)
            decision_data[key] = sibling.strip() if sibling else None
        else:
            decision_data[key] = None

    # Extrair o teor completo da decisão
    teor_decisao = ""
    
    # Verificar se há conteúdo completo da decisão em div com "display: none;"
    hidden_content = soup.find('div', style="display: none;")
    if hidden_content:
        teor_decisao = hidden_content.get_text(separator=" ", strip=True)
    else:
        visible_content = soup.find('div', align='justify')
        teor_decisao = visible_content.get_text(separator=" ", strip=True) if visible_content else ""
    
    decision_data['teor_decisao'] = teor_decisao

    # Se os campos essenciais (classe, assunto, magistrado) ainda estiverem vazios, buscar no teor_decisao
    if not decision_data['classe'] or not decision_data['assunto'] or not decision_data['magistrado']:
        # Busca por "Classe - Assunto"
        classe_assunto_match = re.search(r'Classe - Assunto\s*([\w\s]+)\s*-\s*([\w\s]+)', teor_decisao)
        if classe_assunto_match:
            decision_data['classe'] = classe_assunto_match.group(1).strip()
            decision_data['assunto'] = classe_assunto_match.group(2).strip()

        # Busca por "Magistrado:" primeiro
        magistrado_match = re.search(r'Magistrado:\s*([\w\s]+)', teor_decisao)
        if magistrado_match:
            decision_data['magistrado'] = magistrado_match.group(1).strip()
    
    # Se "magistrado" ainda estiver vazio, buscar por "Juiz de Direito" ou "Juíza de Direito"
    if not decision_data['magistrado']:
        juiz_match = re.search(r'Ju[ií]z\(a\) de Direito:\s*Dr\(a\)\.\s*([\w\s]+)', teor_decisao)
        if juiz_match:
            decision_data['magistrado'] = juiz_match.group(1).strip()

    return decision_data
