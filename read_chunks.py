#creating chunks of text and sending them to the API for embeddings
import requests
import json
import os

#creating a function to create embeddings for a given text
def create_embedding(text):
    r = requests.post("http://localhost:11434/api/embeddings", json={
        "model": "bge-m3",
        "prompt": text
    })
    embedding =  r.json()['embedding']

    return embedding

jsons  = os.listdir("json")
# print(jsons)
for json_file in jsons:
    with open(f"json/{json_file}") as f:
        content = json.load(f)
    for chunk in content['chunks']:
        print(chunk)
    break

# a = create_embedding ("cat sat on the mat.")
# print(a)