# app/templates.py

from langchain.prompts import PromptTemplate

judicial_report_template = """
Ao analisar um processo judicial, siga as instruções abaixo para identificar os pontos essenciais que fundamentam a sentença. Extraia os trechos diretamente do documento, incluindo as citações exatas e fornecendo respostas objetivas para cada pergunta.

**Importante:** Caso um tópico não esteja presente no documento, responda com "Vazio".

Para cada uma das seções abaixo, copie e cole o trecho correspondente ao fundamento da sentença (sem modificar palavras ou frases) logo após o marcador entre colchetes. Inclua a resposta entre aspas, para indicar as citações exatas.

### Questões para Fundamentação da Sentença:

1. [Competência] - "O juiz é competente para analisar o pedido?"
2. [Impugnação à Justiça Gratuita] - "Deve-se analisar a impugnação à justiça gratuita?"
3. [Admissibilidade da Inicial/Inépcia] - "A petição inicial preenche os requisitos de admissibilidade? Há algum motivo de inépcia?"
4. [Legitimidade das Partes] - "A parte autora e ré possuem legitimidade para participar do processo (legitimidade ativa e passiva)?"
5. [Interesse de Agir] - "Há interesse jurídico na pretensão (considerando as facetas de utilidade e adequação)?"
6. [Prescrição e Decadência] - "Há ocorrência de prescrição ou decadência?"
7. [Validade da Citação] - "A citação da parte ré é válida?"
8. [Causas Externas de Extinção do Processo] - "Existem causas externas (ex.: coisa julgada, perempção) que possam levar à extinção do processo?"
9. [Causas Externas de Suspensão do Processo] - "Há causas que justificam a suspensão do processo (ex.: morte de uma das partes, prejudicialidade externa)?"
10. [Defesa/Revelia] - "O réu apresentou defesa válida, ou é caso de revelia?"
11. [Conciliação/Mediação] - "É recomendável determinar a conciliação ou mediação?"
12. [Intervenção de Terceiros] - "Existem terceiros que devem integrar o processo?"
13. [Requerimentos Probatórios] - "As provas requeridas (ex.: oitiva de testemunhas, perícias) devem ser realizadas?"
14. [Julgamento Antecipado] - "Os documentos e provas existentes permitem o julgamento antecipado da pretensão?"
15. [Existência do Direito/Lei Aplicável] - "Qual é a lei aplicável ao pedido do autor? A parte autora possui direito?"
16. [Fatos Constitutivos] - "Quais são os fatos que constituem o direito do autor?"
17. [Fatos Extintivos] - "Existe alguma norma que impede o direito do autor? Quais são os fatos extintivos (defesas) que podem levar ao indeferimento do pedido?"
18. [Liquidação e Quantificação] - "Como devem ser calculados os valores devidos, se aplicável (ex.: danos morais)?"
19. [Litigância de Má-Fé] - "Há indícios de litigância de má-fé?"

**Observação Final:** Baseie-se nas instruções acima para responder de forma precisa e objetiva, incluindo apenas as informações essenciais para cada questão. O modelo deve fornecer respostas contextuais e diretas, sempre verificando se há resposta documentada ou retornando "Vazio" em caso de ausência de informação relevante.

Contexto: {context}

Pergunta: {question}
"""

prompt = PromptTemplate(template=judicial_report_template, input_variables=['context', 'question'])
