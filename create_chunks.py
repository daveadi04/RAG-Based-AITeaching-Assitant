import whisper
import json
import os

# using large model as on github it is mentioned that large model is the best for accuracy and turbo is not adviced.
model = whisper.load_model("large-v2")

audio_files = os.listdir("audios")
for audio_file in audio_files:
    print(audio_file)
    if("_" in audio_file):
        number = audio_file.split("_")[0]
        title = audio_file.split("_")[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio_file}",
        # result = model.transcribe(audio = "audios/4_test.mp3",
                                  language="hi",
                                  task="translate",
                                  without_timestamps=False)

        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

        chunks_with_meta_data = {"chunks": chunks, "text" : result["text"]}
 
        print(chunks)
        with open(f"json/{audio_file}.json", "w") as f:
            json.dump(chunks_with_meta_data, f)