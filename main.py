from ai import AI, Action
from services import Services
from dbcall import Dtbase
import os

services = Services()
ai = AI()
action = Action()
db = Dtbase()


if __name__ == "__main__":
    loginsuccess = action.dbCheck()
    if loginsuccess == True:
        while True:
            query = ai.takeCommand().lower()

            if "time" in query:
                services.clock()
            elif 'date' in query:
                services.date()
            elif 'search wikipedia for' in query:
                services.wikisearch(query)
            elif 'search in chrome' in query:
                services.chromesearch()
            elif 'send mail' in query:
                services.mailService()
            elif 'memory mode' in query:
                ai.speak('Switching to memory mode!!!')
                ai.speak('Begin a phrase with the word remember followed by what you would like me to remember.')
                query = ai.takeCommand().lower()
                if query.startswith('remember'):
                    db.remember(query.replace('remember', ''))
                    ai.speak('Memory saved! Leaving Memory mode')
                elif query.startswith('retrieve'):
                    # implement natural language processing, retrieve memory from database by date and time
                    pass
            elif 'lock' in query:
                os.system('shutdown -l')
            elif 'shutdown' in query:
                os.system('shutdown /s /t 1')
            elif 'restart' in query:
                os.system('shutdown /r /t 1')
            elif 'play music' in query:
                services.music()
            elif 'make a joke' in query:
                services.joke()
            elif 'take a screenshot' in query:
                services.screenshot()
            elif 'cpu'  in query:
                services.cpu()   
            elif 'offline' in query:
                ai.speak("Going offline!")
                quit()

    elif loginsuccess == False:
        ai.speak('You must login to proceed')
        action.dbCheck()

        
    