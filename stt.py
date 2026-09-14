#for trabnslating speach to text
import whisper
import json

# using large model as on github it is mentioned that large model is the best for accuracy and turbo is not adviced.
model = whisper.load_model("large-v2")
result = model.transcribe(audio = "audios/4_test.mp3",
                          language="hi",
                          task="translate",
                          without_timestamps=False)
print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"id" : segment["id"], "start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)
with open("output.json", "w") as f:
    json.dump(chunks,f)