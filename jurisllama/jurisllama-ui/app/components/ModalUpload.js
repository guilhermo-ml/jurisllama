// ModalUpload.js
import { useState } from "react";
import styles from "../page.module.css";

export default function ModalUpload({ onUpload, onClose }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (file) {
      onUpload({ name: file.name });
      onClose(); // Fecha o modal após o upload
    }
  };

  return (
    <div className={styles.modalBackdrop}>
      <div className={styles.modalContent}>
        <h2>Carregar Processo</h2>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} className={styles.uploadButton}>
          Carregar
        </button>
        <button onClick={onClose} className={styles.closeButton}>
          Fechar
        </button>
      </div>
    </div>
  );
}
