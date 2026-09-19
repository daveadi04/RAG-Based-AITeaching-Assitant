import requests
import os
import json
import pandas as pd
 # Create embeddings for a list of texts.
 # met
def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    embedding = r.json()["embeddings"] 
    return embedding

jsons = os.listdir("json")
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"json/{json_file}") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    texts = [c["text"] for c in content["chunks"]]

    embeddings = []

    # Send chunks in batches
    for i in range(0, len(texts), 32):
        batch = texts[i:i + 32]
        embeddings.extend(create_embedding(batch))

    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)

print(df)

# a = create_embedding(["Cat sat on the mat", "Harry dances on a mat"])
# print(a)