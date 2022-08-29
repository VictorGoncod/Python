import speech_recognition as sr

rec = sr.Recognizer()
#print sr.Microphone() as mic:

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou Gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-br")
    print(texto)