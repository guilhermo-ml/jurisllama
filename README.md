# JurisLlama 🦙

> **Project developed for Hackathon Llama Impact Brazil 2024**

JurisLlama is an AI-based legal assistant designed to aid in the analysis of judicial rulings. The system leverages advanced language models to process legal documents, offering valuable insights to streamline the creation and review of rulings, enabling fast and detailed analysis of legal cases.

## 🚀 Project Objective

The objective of JurisLlama is to optimize time and accuracy in judicial case analysis by providing a system capable of:

1. **Reading and interpreting judicial rulings** from PDFs.
2. **Summarizing and extracting essential information** from decisions, facilitating the reuse of arguments.
3. **Searching for related jurisprudence**, offering relevant insights for new judicial decisions.

## 🛠️ System Architecture

JurisLlama is composed of various technologies that form an integrated and optimized architecture for legal analysis:

- **FastAPI**: Backend for API management and exposure.
- **Groq and Llama**: Inference models for natural language processing, using Llama 3.2 for legal text analysis.
- **LangChain and ChromaDB**: Support for vector storage and retrieval, allowing quick and contextualized queries in a database of judicial decisions.
- **HTML-Parser**: Extracts data and content from HTML files of judicial decisions.
- **API in R with Plumber**: Connected to TJSP (São Paulo State Court) to directly retrieve case information.
- **MongoDB**: Database for storage and management of case data.
- **Llama-Parser**: Processes and interprets PDF files sent by the user, structuring the data for analysis.

## ⚙️ Technologies Used

- **FastAPI**: For building RESTful APIs.
- **Groq**: Optimized hardware infrastructure for running AI models.
- **Llama 3.2**: Language model for interpreting and analyzing legal documents.
- **LangChain**: Organizes and stores information in contextual memory.
- **ChromaDB**: Vector database for efficient information retrieval.
- **Next.js**: User interface for visualizing and interacting with the system.
- **HTML-Parser**: Tool for extracting data from HTML judicial decisions.
- **Plumber (R)**: API for retrieving data directly from TJSP.
- **MongoDB**: Stores collected case data for persistent storage and quick retrieval.
- **Llama-Parser**: Processes PDFs on the judge's frontend for detailed analysis.

## 📝 Key Features

1. **PDF Upload**: Upload legal documents for analysis and processing by the Llama-Parser.
2. **Ruling Summarization**: Generates a structured summary of key information extracted from judicial decisions.
3. **Jurisprudence Search**: Searches previous rulings based on the context of the uploaded decision.
4. **Integration with TJSP**: Retrieves case data directly from the São Paulo State Court via the Plumber API in R.
5. **User Interface**: Next.js frontend for intuitive navigation and result visualization.
6. **Storage and Retrieval in MongoDB**: Manages extracted case data for persistent storage and quick queries.

## ⚡ How to Run JurisLlama

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/jurisllama.git
   cd jurisllama

#Português

# JurisLlama 🦙

> **Projeto desenvolvido para o Hackathon Llama Impact Brasil 2024**

JurisLlama é um assistente jurídico baseado em IA projetado para auxiliar na análise de decisões judiciais. O sistema utiliza modelos de linguagem avançados para processar documentos legais, oferecendo insights valiosos para agilizar a criação e revisão de sentenças, permitindo uma análise rápida e detalhada de casos jurídicos.

## 🚀 Objetivo do Projeto

O objetivo do JurisLlama é otimizar o tempo e a precisão na análise de processos judiciais, disponibilizando um sistema capaz de:

1. **Leitura e interpretação de decisões judiciais** em PDFs.
2. **Resumir e extrair informações essenciais** das decisões, facilitando a reutilização de argumentos.
3. **Buscar jurisprudência relacionada**, oferecendo insights relevantes para novas decisões judiciais.

## 🛠️ Arquitetura do Sistema

JurisLlama é composto por várias tecnologias que formam uma arquitetura integrada e otimizada para análise jurídica:

- **FastAPI**: Backend para gerenciamento e exposição de APIs.
- **Groq e Llama**: Modelos de inferência para processamento de linguagem natural, usando Llama 3.2 para análise de textos jurídicos.
- **LangChain e ChromaDB**: Suporte para armazenamento e recuperação de vetores, permitindo consultas rápidas e contextualizadas em uma base de dados de decisões judiciais.
- **HTML-Parser**: Extrai dados e conteúdo de arquivos HTML de decisões judiciais.
- **API em R com Plumber**: Conectada ao TJSP para buscar processos diretamente do sistema do Tribunal de Justiça de São Paulo.
- **MongoDB**: Banco de dados para armazenamento e gerenciamento dos processos.
- **Llama-Parser**: Processa e interpreta arquivos PDF enviados pelo usuário, estruturando os dados para análise.

## ⚙️ Tecnologias Utilizadas

- **FastAPI**: Para construção de APIs RESTful.
- **Groq**: Infraestrutura de hardware otimizada para execução de modelos de IA.
- **Llama 3.2**: Modelo de linguagem para interpretação e análise de documentos jurídicos.
- **LangChain**: Organização e armazenamento de informações em uma memória contextual.
- **ChromaDB**: Banco de dados vetorial para recuperação eficiente de informações.
- **Next.js**: Interface de usuário para visualização e interação com o sistema.
- **HTML-Parser**: Ferramenta para extrair dados de HTMLs de decisões.
- **Plumber (R)**: API para buscar dados diretamente no TJSP.
- **MongoDB**: Armazena os processos coletados para consultas rápidas e persistentes.
- **Llama-Parser**: Processa PDFs no frontend do juiz para análise detalhada.

## 📝 Funcionalidades Principais

1. **Upload de PDF**: Envie documentos jurídicos para análise e processamento pelo Llama-Parser.
2. **Resumo de Sentenças**: Geração de um resumo estruturado das principais informações extraídas das decisões judiciais.
3. **Pesquisa de Jurisprudências**: Consulta a decisões anteriores com base no contexto da sentença enviada.
4. **Integração com o TJSP**: Busca de processos no Tribunal de Justiça de São Paulo através da API em R com Plumber.
5. **Interface de Usuário**: Frontend em Next.js para navegação intuitiva e visualização dos resultados.
6. **Armazenamento e Recuperação em MongoDB**: Gestão de dados dos processos extraídos para armazenamento persistente e consultas rápidas.

## ⚡ Como Executar o JurisLlama

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/jurisllama.git
   cd jurisllama

