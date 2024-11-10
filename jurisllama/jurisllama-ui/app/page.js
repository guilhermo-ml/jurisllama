"use client";

import { useState, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import Chatbox from "./components/Chatbox";
import ModalUpload from "./components/ModalUpload";
import styles from "./page.module.css";

export default function HomePage() {
  const [processes, setProcesses] = useState([]);
  const [selectedProcess, setSelectedProcess] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(true);
  const [isChatEnabled, setIsChatEnabled] = useState(false);
  const [inputText, setInputText] = useState("");
  const [showSearchSuggestion, setShowSearchSuggestion] = useState(false);

  const handleUpload = (process) => {
    const newProcess = {
      id: processes.length + 1,
      name: process.name || `Processo ${processes.length + 1}`,
      messages: [{ sender: "bot", text: "Processo carregado com sucesso. Como posso ajudar?" }],
    };
    setProcesses([...processes, newProcess]);
    setSelectedProcess(newProcess.id);
    setIsModalOpen(false);
    setIsChatEnabled(true);
  };

  const handleProcessSelect = (processId) => {
    setSelectedProcess(processId);
    setIsChatEnabled(true);
  };

  const handleNewProcess = () => {
    setIsModalOpen(true);
    setIsChatEnabled(false);
  };

  const handleSendMessage = async (question) => {
    if (!isChatEnabled || !selectedProcess) return;

    // Adiciona a mensagem do usuário ao chat
    setProcesses((prevProcesses) =>
      prevProcesses.map((process) =>
        process.id === selectedProcess
          ? {
              ...process,
              messages: [...process.messages, { sender: "user", text: question }],
            }
          : process
      )
    );

    // Verifica se o comando de pesquisa foi utilizado
    const isSearchQuery = question.toLowerCase().startsWith("/pesquisar ");
    const endpoint = isSearchQuery ? "search-decisions" : "query";
    const searchTerm = isSearchQuery ? question.replace("/pesquisar ", "").trim() : question;

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/${endpoint}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: searchTerm }),
      });

      if (!response.ok) {
        throw new Error("Erro ao obter resposta do backend");
      }

      const data = await response.json();

      const botMessage = isSearchQuery
        ? data.decisions && Array.isArray(data.decisions)
          ? data.decisions.map(
              (dec) =>
                `Processo: <a href="${dec.link}" target="_blank">${dec.processo}</a><br>Teor da Decisão: ${dec.teor_decisao}`
            ).join("<br><br>")
          : "Nenhuma decisão relevante encontrada."
        : data.answer || "O modelo não forneceu uma resposta.";

      setProcesses((prevProcesses) =>
        prevProcesses.map((process) =>
          process.id === selectedProcess
            ? {
                ...process,
                messages: [...process.messages, { sender: "bot", text: botMessage }],
              }
            : process
        )
      );
    } catch (error) {
      console.error("Erro ao obter resposta do backend:", error);
      setProcesses((prevProcesses) =>
        prevProcesses.map((process) =>
          process.id === selectedProcess
            ? {
                ...process,
                messages: [
                  ...process.messages,
                  { sender: "bot", text: "Ocorreu um erro ao processar sua solicitação." },
                ],
              }
            : process
        )
      );
    }
  };

  // Detecta o comando de pesquisa
  useEffect(() => {
    if (inputText.startsWith("/")) {
      setShowSearchSuggestion(inputText.toLowerCase().startsWith("/pesquisar") ? false : true);
    } else {
      setShowSearchSuggestion(false);
    }
  }, [inputText]);

  const currentMessages = processes.find((process) => process.id === selectedProcess)?.messages || [];

  return (
    <div className={styles.container}>
      {isModalOpen && <ModalUpload onUpload={handleUpload} onClose={() => setIsModalOpen(false)} />}
      <Sidebar processes={processes} onSelectProcess={handleProcessSelect} onNewProcess={handleNewProcess} />
      <div className={styles.chatContainer}>
        <Chatbox messages={currentMessages} />
        <div className={styles.inputContainer}>
          <input
            type="text"
            className={styles.input}
            placeholder="Digite sua pergunta..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSendMessage(inputText);
                setInputText(""); // Limpa o campo após enviar a mensagem
              }
            }}
            disabled={!isChatEnabled}
          />
          <button
            onClick={() => {
              handleSendMessage(inputText);
              setInputText(""); // Limpa o campo após enviar a mensagem
            }}
            className={styles.button}
            disabled={!isChatEnabled}
          >
            Enviar
          </button>
        </div>
        {/* Sugestão de Comando */}
        {showSearchSuggestion && (
          <div className={styles.suggestion}>
            Dica: Digite <strong>/pesquisar [termo]</strong> para buscar decisões
          </div>
        )}
      </div>
    </div>
  );
}
