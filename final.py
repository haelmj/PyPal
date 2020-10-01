import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
# import psuti



class AI:
    engine = pyttsx3.init()


    def __init__(self, name, language, gender):
        self.name = name
        self.language = language
        self.gender = gender
        return

    @staticmethod
    def speak(audio):
        AI.engine.say(audio)
        AI.engine.runAndWait()

    def takeCommand(self):
        r = sr.Recognizer() # initialize the listener
        m = sr.Microphone()
        with m as source: # set listening device to microphone
            print("Listening...")
            r.pause_threshold = 1 # delay one second from program start before listening
            audio= r.listen(source)

        try:
            print("Voice Recognition in process...")
            query = r.recognize_google(audio, language='en-UK') #listen to audio
            print(query)
        
        except Exception as e:
            print(e)
            self.speak("Say that again please...")
            query = self.takeCommand()
        return query
