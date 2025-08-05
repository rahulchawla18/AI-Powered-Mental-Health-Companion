import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
collection = client.get_or_create_collection("journal_entries")

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

memory = []

def add_to_store(username, text, emotion, feedback, timestamp):
    entry_id = f"{username}_{len(memory)+1}"
    memory.append({"id": entry_id, "username": username, "text": text, "emotion": emotion, "feedback": feedback, "timestamp": timestamp})
    collection.add(
        ids=[entry_id],
        documents=[text],
        metadatas=[{"username": username, "emotion": emotion, "timestamp": timestamp}]
    )

def get_all_entries(username):
    return [e for e in memory if e["username"] == username]

def semantic_search(username, query):
    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={"username": username}
    )
    return results["documents"][0] if results["documents"] else []