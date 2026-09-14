#for trabnslating speach to text
import whisper
# using large model as on github it is mentioned that large model is the best for accuracy and turbo is not adviced.
model = whisper.load_model("large-v2")
result = model.transcribe(audio = "audios/6_SEO and Core Web Vitals in HTML.mp3.mp3",
                          translate=True,
                          language="hi")
print(result["text"])