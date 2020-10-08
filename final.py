import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import dbcall as db
import time
from assets.fileexplorer import fileExplorer
from assets.popup import passpopup, popup
# import psuti



class AI:
    engine = pyttsx3.init()
    db = db.Dtbase()
    db.queryDb()

    def __init__(self):
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

class Action(AI):
    
    def wishMe(self):
        speak = self.speak
        user = AI.db.username
        ai_call = AI.db.ai_name
        speak(f"Hello {user}! Welcome back!")
        hour = int(datetime.datetime.now().hour)
        if hour >= 6 and hour < 12:
            speak("Good morning!")
        elif 12 <= hour < 18:
            speak("Good afternoon!") 
        elif hour >= 18 and hour < 24:
            speak("Good evening!")
        else:
            speak("Having trouble sleeping?") 
        speak(f"{ai_call} is ready to help you! What would you like?")

    def userLogin(self):
        speak = self.speak
        speak(f'Login Attempt! {AI.db.username}, please state the passcode!')
        # add code to take the passcode and compare it with what is in the database
        pwd = self.takeCommand().lower()
        logincount = 1
        loginsuccess = False
        while loginsuccess == False and logincount < 5:
            value = AI.db.pwdcompare(pwd)
            if value == 1:
                speak('Login Attempt Successful!')
                loginsuccess = True
                self.wishMe()
            elif (value != 1): 
                speak("That wasn't the passcode you have 3 attempts left!")
                logincount += 1
                speak('Please State The Passcode')
                pwd = self.takeCommand().lower()
                if loginsuccess == False and logincount == 3: 
                    speak('You have reached the maximum number of login attempts! Try again in 30 seconds')
                    time.sleep(30)
                    self.userLogin()
        return loginsuccess

    def setupMail(self, username):
        speak = self.speak
        speak('Please enter your gmail address!')
        email_address = popup('Email', 'Please type in your gmail address!')
        speak('''Please enter your password. If you have set up two factor authentication on your google account, then this should be your app password.\
            Otherwise you should enter your gmail password.''')
        email_password = passpopup('Password', 'Password:')
        speak('If you used your gmail password, please ensure that you have configured your google account to accept connections from less secure apps!!')
        AI.db.setupMail(email_address, email_password, username)
        time.sleep(5)
        AI.db.queryDb()
        return

    def setupUser(self):
        speak = self.speak
        speak("Hello User. I will be your virtual assistant. I'd like to get to know you! What is your name?")
        user_name = self.takeCommand()
        speak(f'Hello {user_name}. What would you like to call me?')
        ai_call = self.takeCommand()
        speak(f'{ai_call} at your service! To protect your data, please provide a passphrase that will be used to access me!')
        passconfirmation = False
        while passconfirmation == False:
            passphrase = self.takeCommand().lower()
            speak('Please confirm your passphrase by stating it again!')
            passphrase2 = self.takeCommand().lower()
            if passphrase == passphrase2:
                speak('Passphrase Confirmed!')
                passconfirmation = True   
            else:
                speak("I had issues confirming the passphrase. Let's try that again. Please state the passphrase!")
                continue
        AI.db.setupApp(ai_call,user_name, passphrase) # pass user details to db
        speak('Would you like to configure gmail address for mailing services?')
        user_choice = self.takeCommand()
        if user_choice == 'yes':
            self.setupMail(user_name)
            AI.db.queryDb()
            self.userLogin()
        else:
            speak('Skipping Mail Configuration...')
            speak("If you would like to configure at a later time, say 'Configure Mail'")
            AI.db.queryDb()    
            self.userLogin()        
        return

    def dbCheck(self):
        if AI.db.ai_name == '' or AI.db.username == '':
            AI.db.dbreset()
            self.setupUser()
        else:
            loginsuccess = self.userLogin()
            return loginsuccess  


Action().dbCheck()