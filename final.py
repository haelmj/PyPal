import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


class AI:
    engine = pyttsx3.init()


    def __init__(self, name, engine, language, gender):
        self.name = name
        self.engine = engine
        self.language = language
        self.gender = gender
        return

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        r = sr.Recognizer() # initialize the listener
        with sr.Microphone() as source: # set listening device to microphone
            print("Listening...")
            r.pause_threshold = 1 # delay one second from program start before listening
            audio= r.listen(source)

        try:
            print("Voice Recognition in process...")
            query = r.recognize_google(audio, language='en-US') #listen to audio
            print(query)
        
        except Exception as e:
            print(e)
            speak("Say that again please...")
            return
        return query
