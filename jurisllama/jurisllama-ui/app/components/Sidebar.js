import Image from "next/image";
import styles from "../page.module.css";

export default function Sidebar({ processes, onSelectProcess, onNewProcess }) {
  return (
    <div className={styles.sidebar}>
      <Image src="/v0.01.png" alt="Logo" width={180} height={180} />
      <h2>Processos</h2>
      <ul>
        {processes.map((process) => (
          <li key={process.id} onClick={() => onSelectProcess(process.id)}>
            {process.name}
          </li>
        ))}
      </ul>
      <button onClick={onNewProcess} className={styles.newProcessButton}>
        Novo Processo
      </button>
    </div>
  );
}
