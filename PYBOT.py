import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
import json
import requests


print('Loading your AI personal assistant - PYBOT')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def CommandMe():
    speak("To Know About me: ask who are you")
    print("To Know About me: ask who are you")
    speak("To know about my creator: ask who created you")
    print("To know about my creator: ask who created you")
    speak("To open Youtube: say open youtube")
    print("To open Youtube: say open youtube")
    speak("To open Google: say open google")
    print("To open Google: say open google")
    speak("To open Gmail: say open gmail")
    print("To open Gmail: say open gmail")
    speak("To know the current time: ask what is the time")
    print("To know the current time: ask what is the time")
    speak("To know the current news: what is the news")
    print("To know the current news: what is the news")
    speak("To search anything: ask search for .....")
    print("To search anything: ask search for .....")
    speak("To exit PYBOT: say ok bye or stop")
    print("To exit PYBOT: say ok bye or stop")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant PYBOT")
wishMe()

CommandMe()
if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant PYBOT is shutting down,Good bye')
            print('your personal assistant PYBOT is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement:
            speak('I am PYBOT version 1 point O your persoanl assistant, built by Yuvika Gautam. I am programmed to do task such to ease your life and make your work easier.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by YUVIKA GAUTAM")
            print("I was built by YUVIKA GAUTAM")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        # elif "camera" in statement or "take a photo" in statement:
        #     ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "log off" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
