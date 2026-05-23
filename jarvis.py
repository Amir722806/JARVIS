import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",150)
# engine.say("Hello Aqsa How are You")
# engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def command():
    content=" "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


# recognize speech using Google Speech Recognition
        try:
            content= r.recognize_google(audio, lenguage='en-in')
            print("You Said..............." + content )
        except Exception as e:
            print("Please Try Again...")

    return content

def main_process():
    while True:
        request=command().lower()
        if "hello" in request:
            speak("Welcome, How i Can Help You...")
        elif "play music" in request:
            speak("Playing Music")
            song=random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=J1d4nCXNlDs&list=RDJ1d4nCXNlDs&start_radio=1&t=2677s")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=Mrv_YjesdFU&list=RDMrv_YjesdFU&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=CLzPhmhHsP8&list=RDCLzPhmhHsP8&start_radio=1")
        elif "now time" in request:
            now_time = datetime.datetime.now()
            speak("Current Time is "+ now_time)

main_process()
       