import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import dbcall2 as d
import time

db = d.Dtbase()
db.queryDb()
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer() # initialize the listener
    with sr.Microphone() as source: # set listening device to microphone
        print("Listening...")
        r.pause_threshold = 1 # delay one second from program start before listening
        r.adjust_for_ambient_noise(source, duration=1)
        audio= r.listen(source)    

    try:
        print("Voice Recognition in process...")
        query = r.recognize_google(audio, language='en-UK') #listen to audio
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        takeCommand()
    return query

def wishMe():
    user = db.username
    ai_call = db.ai_name
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

def userLogin():
    speak(f'Login Attempt! {db.username}, please state the passcode!')
    # add code to take the passcode and compare it with what is in the database
    pwd = takeCommand().lower()
    logincount = 1
    loginsuccess = False
    while loginsuccess == False and logincount < 5:
        if pwd == db.passcode:
            speak('Login Attempt Successful!')
            loginsuccess = True
            wishMe()
        elif (pwd != db.passcode): 
            speak("That wasn't the passcode you have 3 attempts left!")
            logincount += 1
            speak('Please State The Passcode')
            pwd = takeCommand().lower()
            if loginsuccess == False and logincount == 3: 
                speak('You have reached the maximum number of login attempts! Try again in 30 seconds')
                time.sleep(30)
                userLogin()
    return loginsuccess

def setupUser():
    speak("Hello User. I will be your virtual assistant. I'd like to get to know you! What is your name?")
    user_name = takeCommand()
    speak(f'Hello {user_name}. What would you like to call me?')
    ai_call = takeCommand()
    speak(f'{ai_call} at your service! To protect your data, please provide a passphrase that will be used to access me!')
    passconfirmation = False
    while passconfirmation == False:
        passphrase = takeCommand().lower()
        speak('Please confirm your passphrase by stating it again!')
        passphrase2 = takeCommand().lower()
        if passphrase == passphrase2:
            speak('Passphrase Confirmed!')
            passconfirmation = True   
        else:
            speak("I had issues confirming the passphrase. Let's try that again. Please state the passphrase!")
            continue
    db.setupApp(ai_call,user_name, passphrase) # run pass arguments into the setup app for insertion to database
    db.queryDb()    
    userLogin()        
    return

def clock():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"The current date is {day}, {month}, {year}")

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\projects\\AI\\screenshots\\ss.png') # alter process

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'CPU is at {usage}')
    battery = psutil.sensors_battery()
    speak('Battery is at ' + battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def dbCheck():
    if db.ai_name == '' or db.username == '':
        db.dbreset()
        setupUser()
    else:
        userLogin()
    return   


if __name__ == "__main__":
    dbCheck()
    if True:
        while True:
            query = takeCommand().lower()

            if "time" in query:
                clock()
            elif 'date' in query:
                date()
            elif 'wikipedia' in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
        
            elif 'search in chrome' in query:
                speak('What should I search for?')
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower() #not working yet
                wb.get(chromepath).open_new_tab(search)
            
            elif 'lock' in query:
                os.system('shutdown -l')
            
            elif 'shutdown' in query:
                os.system('shutdown /s /t 1')
            
            elif 'restart' in query:
                os.system('shutdown /r /t 1')
            
            elif 'play songs' in query:
                songs_dir = 'C:/Users/Michael J/Music'
                songs = os.listdir(songs_dir)
                for song in songs:
                    os.startfile(os.path.join(songs_dir, song))

            elif 'take a screenshot' in query:
                screenshot()
                speak('Your screenshot has been taken!!!')

            elif 'cpu '  in query:
                cpu()
            
            elif 'joke' in  query:
                jokes()
            
            elif 'offline' in query:
                speak("Going offline!")
                quit()

    elif userLogin() == False:
        speak('You must login to proceed')
        dbCheck()

# ToDO
# verify functions
# Pass loginsuccess for external use
# Alter functions with embedded paths
# Encrypt password and reconfirm password validation
# Enable password recovery
# configure email for user
# configure memory on data function

    