JurisLlama 🦙
Projeto desenvolvido para o Hackathon Llama Impact Brazil 2024

JurisLlama é um assistente jurídico baseado em inteligência artificial, criado para auxiliar na análise de sentenças judiciais. O sistema utiliza modelos avançados de linguagem para processar documentos legais e oferece insights valiosos para acelerar a criação e revisão de sentenças, permitindo uma análise rápida e detalhada de casos jurídicos.

🚀 Objetivo do Projeto
O objetivo do JurisLlama é otimizar o tempo e a precisão na análise de processos judiciais, fornecendo um sistema capaz de:

Ler e interpretar sentenças jurídicas a partir de PDFs.
Resumir e extrair informações importantes das decisões, facilitando a reutilização de argumentos.
Buscar jurisprudências relacionadas, oferecendo insights relevantes para novas decisões judiciais.
🛠️ Arquitetura do Sistema
O JurisLlama é composto por três principais tecnologias:

FastAPI: Backend para manipulação e exposição das APIs.
Groq e Llama: Modelos de inferência para processamento de linguagem natural, usando Llama 3.2 para análise de textos jurídicos.
LangChain e ChromaDB: Suporte para armazenamento e recuperação de vetores, permitindo consultas rápidas e contextualizadas em uma base de dados de decisões judiciais.
⚙️ Tecnologias Utilizadas
FastAPI: Para construção das APIs RESTful.
Groq: Infraestrutura de hardware otimizada para execução de modelos de IA.
Llama 3.2: Modelo de linguagem para interpretação e análise de documentos jurídicos.
LangChain: Organização e armazenamento de informações em uma memória de contexto.
ChromaDB: Banco de dados vetorial para recuperação de informações.
Next.js: Interface de usuário para visualização e interação com o sistema.
📝 Funcionalidades Principais
Upload de PDF: Envie documentos jurídicos para análise.
Resumo de Sentenças: Geração de um resumo estruturado das principais informações.
Busca de Jurisprudências: Consulta a decisões anteriores com base no contexto da sentença.
Interface de Usuário: Frontend em Next.js para navegação intuitiva e visualização dos resultados.
