import speech_recognition as sr
import playsound 
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os


class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name
        
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''
        
    def engine_speak(self, text):
        
        #fala da assistente virtual
        
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()
        
    def record_audio(self, ask=""):
        
        with sr.Microphone() as source:
            if ask:
                print('Ouvindo...')
                self.engine_speak(ask)
                
            audio = self.r.listen(source,5 , 5)
            print('Olhando para o banco de dados')
            
            try:
                self.voice_data = self.r.recognize_google(audio ,language='pt-BR')
            except sr.UnknownValueError:
                self.engine_speak("Desculpe chefe, não entendi o que você disse. Por favor, pode repetir?")
            except sr.RequestError:
                self.engine_speak("Desculpe chefe, meu servidor está inativo")
                
            print(">>", self.voice_data.lower())
            self.voice_data = self.voice_data.lower()
            
            return self.voice_data.lower()
        
    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='pt')
        r = random.randint(1,200000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assist_name + ':', audio_strig)
        os.remove(audio_file)
        
    def there_exist(self, terms):
        
        #função para identificar si o termo existe
        
        for term in terms:
            if term in self.voice_data:
                return True
            
    def respond(self, voice_data):
        if self.there_exist(['oi', 'hi','holla']):
            greetigns = [f'Oi {self.person}, o que vamos fazer hoje?'
                         'Oi chefe, como posso ajudá-lo?',
                         'Oi chefe, o que você precisa?']
            greet = greetigns[random.randint(0, len(greetigns)-1)]
            self.engine_speak(greet)
         
        #Google    
        if self.there_exist(['procurar por']) and 'youtube' not in voice_data:
            search_term =voice_data.split("por")[-1]
            url ='http://google.com/search?q=' + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para" + search_term + 'no google')
            
        #Youtube
        if self.there_exist(['procure no youtube por']):
            search_term =voice_data.split("por")[-1]
            url ='http://www.youtube.com/results?search_query=' + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para" + search_term + 'no youtube')
            
assistent = Virtual_assit('Alexa', 'Victor')

while True:
    
    voice_data = assistent.record_audio('ouvindo...')
    assistent.respond(voice_data)
    
    if assistent.there_exist(['tchau', 'adeus', 'te vejo mais tarde']):
        assistent.engine_speak("Tenha um bom dia! Adeus!")
        break
        