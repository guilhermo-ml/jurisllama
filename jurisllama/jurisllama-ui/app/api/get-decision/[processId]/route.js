// app/api/get-decision/[processId]/route.js
import { MongoClient } from "mongodb";

const MONGO_URI = "mongodb://localhost:27017";
const DATABASE_NAME = "decisoes_tjsp";
const COLLECTION_NAME = "primeiro_grau";

export async function GET(req, { params }) {
  const { processId } = params;

  const client = new MongoClient(MONGO_URI);
  try {
    await client.connect();
    const db = client.db(DATABASE_NAME);
    const collection = db.collection(COLLECTION_NAME);
    const decision = await collection.findOne({ processo: processId });

    if (!decision) {
      return new Response(JSON.stringify({ error: "Decisão não encontrada" }), { status: 404 });
    }

    return new Response(JSON.stringify(decision), { status: 200 });
  } catch (error) {
    console.error("Erro ao buscar decisão:", error);
    return new Response(JSON.stringify({ error: "Erro interno ao buscar decisão" }), { status: 500 });
  } finally {
    await client.close();
  }
}
