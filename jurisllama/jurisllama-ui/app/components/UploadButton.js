import styles from "../page.module.css";

export default function UploadButton({ onUpload }) {
  const handleUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append("file", file);
      
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/upload-pdf/`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      onUpload(data);
    }
  };

  return (
    <input type="file" onChange={handleUpload} className={styles.button} />
  );
}
