import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import requests
from PyDictionary import PyDictionary

listener=sr.Recognizer()
machine=pyttsx3.init()
voices=machine.getProperty('voices')
machine.setProperty('voice',voices[1].id)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'elena' in command:
                command=command.replace('elena','')
                print(command)
    except:
        pass
    return command

while True:
    def run_elena():
        command =take_command()
        print(command)
        if 'play' in command:
            song=command.replace('play','')
            talk("Playing "+song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            about=command.replace('tell me about','')
            info=wikipedia.summary(about,sentences=5)
            print(info)
            talk(info)
        elif 'meaning of' in command:
            mean=command.replace('meaning of','')
            means=PyDictionary()
            meanof=means.meaning(mean)
            print(meanof)
            talk(meanof)
        elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            talk("current time is")
            print(time)
            talk(time)
        elif 'date' in command:
            date=datetime.date.today()
            print(date)
            talk(date)
        elif 'who is' in command:
            about = command.replace('who is', '')
            info = wikipedia.summary(about,sentences=5)
            print(info)
            talk(info)
        elif 'news' in command:
            import requests
            def new():
                main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=25ff1e2bd18f41a49339ac7c520b45e3"
                news=requests.get(main_url).json()
                article=news['articles']
                news_article=[]
                for arti in article:
                    news_article.append(arti['description'])
                for i in range(1):
                    print(news_article[i])
                    talk(news_article[i])
            new()
        
        elif 'hello' in command:
            greetings="Hello! I am Elena"
            question='What can i do for you?'
            print(greetings)
            talk(greetings)
            print(question)
            talk(question)
    
        elif 'stop' in command:
            bye="Bye have a cute day"
            print(bye)
            talk(bye)
        else:
            print("Sorry can you please repeat the command")
    
    run_elena()
    




