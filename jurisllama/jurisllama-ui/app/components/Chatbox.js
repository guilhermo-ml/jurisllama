// components/Chatbox.js
import styles from "../page.module.css";
import Link from "next/link";

export default function Chatbox({ messages }) {
  return (
    <div className={styles.chatbox}>
      {messages.map((msg, index) => (
        <div
          key={index}
          className={msg.sender === "user" ? styles.userMessage : styles.botMessage}
          {...(msg.sender === "bot"
            ? { dangerouslySetInnerHTML: { __html: formatMessage(msg.text) } }
            : { children: <p>{msg.text}</p> })}
        />
      ))}
    </div>
  );
}

// Função para formatar mensagens com links e questões para fundamentação da sentença
function formatMessage(text) {
  // Detecta se é uma lista de questões para fundamentação da sentença
  if (text.includes("Aqui estão as respostas às questões para fundamentação da sentença")) {
    return formatSentencaMessage(text);
  }

  // Formata mensagens com links de processos para decisões de pesquisa
  return formatDecisionMessage(text);
}

// Função para formatar mensagens de decisões com links e parágrafos
function formatDecisionMessage(text) {
  return text
    .split(/\n+/) // Quebra por linhas ou parágrafos
    .map((line) => {
      // Adiciona links para qualquer número de processo encontrado
      return line.replace(
        /Processo:\s(\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4})/g,
        '<a href="/view-decision/$1" class="processLink">Processo: $1</a>'
      );
    })
    .map((line) => `<p>${line}</p>`) // Transforma cada linha formatada em parágrafo
    .join("");
}

// Função para formatar mensagens de fundamentação da sentença
function formatSentencaMessage(text) {
  return text
    .split(/(\d+\.\s)/) // Quebra por número de cada questão
    .filter(Boolean) // Remove partes vazias
    .map((part, idx, arr) => {
      // Adiciona o número e o conteúdo de cada questão
      if (/\d+\.\s/.test(part)) {
        return `<p><strong>${part.trim()}</strong>${arr[idx + 1]}</p>`;
      }
      return "";
    })
    .join("");
}
