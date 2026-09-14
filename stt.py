#for trabnslating speach to text
import whisper
# using large model as on github it is mentioned that large model is the best for accuracy and turbo is not adviced.
model = whisper.load_model("large-v2")
result = model.transcribe(audio = "audios/4_test.mp3",
                          language="hi",
                          task="translate")
print(result["text"])