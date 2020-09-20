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

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"The current date is {day}, {month}, {year}")

def wishMe():
    speak("Welcome back Michael!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good morning Michael!")
    elif 12 <= hour < 18:
        speak("Good afternoon Michael!") 
    elif hour >= 18 and hour < 24:
        speak("Good evening Michael!")
    else:
        speak("Having trouble sleeping?") 
    speak("Sarah is ready to help you! What would you like?")

def takeCommand():
    r = sr.Recognizer() # initialize the listener
    with sr.Microphone() as source: # set listening device to microphone
        print("Listening...")
        r.pause_threshold = 1 # delay one second from program start before listening
        r.adjust_for_ambient_noise(source, duration=1) #adjust energy threshold based on the surrounding noise level 
        audio= r.listen(source)

    try:
        print("Voice Recognition in process...")
        query = r.recognize_google(audio, language='en-UK') #listen to audio
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        query = takeCommand()
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\projects\\AI\\screenshots\\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'CPU is at {usage}')
    battery = psutil.sensors_battery()
    speak('Battery is at ' + battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = 'manj19.mjn@gmail.com'
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Unable to send the email')
        
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

        elif 'remember that' in query:
            speak('What should I remember?')
            data = takeCommand()
            speak('You said I should remember that' + data)
            speak('Did I get that right?')
            confirm = takeCommand()
            if confirm == 'yes' or confirm == 'yeah':
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
                speak('Your data has been committed to memory!')
            elif confirm == 'no':
                speak('Oops, Sorry about that!Try again')

        elif 'Did you remember anything' in query:
            remember = open('data.txt', 'r')
            speak('You asked me to remember that ' + remember.read()) #modify to say something different if nothing was remembered            
        
        elif 'take a screenshot' in query:
            screenshot()
            speak('Your screenshot has been taken!!!')

        elif 'cpu ' in query:
            cpu()
        
        elif 'joke' in  query:
            jokes()
        
        elif 'offline' in query:
            speak("Going offline!")
            quit()
        
        