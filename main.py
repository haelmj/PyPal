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
            elif query.startswith('remember'):
                db.remember(query.replace('remember', ''))
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

# can replace the other function in absence of database
#         elif 'remember that' in query:
#             speak('What should I remember?')
#             data = takeCommand()
#             speak('You said I should remember that' + data)
#             speak('Did I get that right?')
#             confirm = takeCommand()
#             if confirm == 'yes' or confirm == 'yeah':
#                 remember = open('data.txt', 'w')
#                 remember.write(data)
#                 remember.close()
#                 speak('Your data has been committed to memory!')
#             elif confirm == 'no':
#                 speak('Oops, Sorry about that!Try again')

#         elif 'Did you remember anything' in query:
#             remember = open('data.txt', 'r')
#             speak('You asked me to remember that ' + remember.read()) #modify to say something different if nothing was remembered            
        
    