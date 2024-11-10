import formidable from "formidable";
import fs from "fs";

export const config = { api: { bodyParser: false } };

export default async function handler(req, res) {
  const form = new formidable.IncomingForm();
  form.parse(req, (err, fields, files) => {
    if (err) return res.status(500).json({ error: err });
    const fileData = fs.readFileSync(files.file.filepath);
    // Simulação de processamento
    res.status(200).json({ name: files.file.originalFilename });
  });
}
