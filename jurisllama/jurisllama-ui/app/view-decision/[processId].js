// app/view-decision/[processId].js
import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import styles from "../page.module.css";

export default function DecisionView() {
  const router = useRouter();
  const { processId } = router.query;
  const [decision, setDecision] = useState(null);

  useEffect(() => {
    if (!processId) return;

    const fetchDecision = async () => {
      try {
        const response = await fetch(`/api/get-decision/${processId}`);
        const data = await response.json();
        setDecision(data);
      } catch (error) {
        console.error("Erro ao obter a decisão:", error);
      }
    };

    fetchDecision();
  }, [processId]);

  if (!decision) {
    return <div className={styles.loading}>Carregando decisão...</div>;
  }

  return (
    <div className={styles.decisionContainer}>
      <h2 className={styles.decisionTitle}>Processo: {decision.processo}</h2>
      <div
        className={styles.decisionContent}
        dangerouslySetInnerHTML={{ __html: formatDecisionText(decision.teor_decisao) }}
      />
    </div>
  );
}

// Função para formatar o texto da decisão
function formatDecisionText(text) {
  return text
    .split(/\n{2,}/) // Quebra em blocos de duas quebras de linha
    .map((paragraph) => `<p>${paragraph.trim()}</p>`)
    .join(""); // Cria tags <p> para cada bloco
}
