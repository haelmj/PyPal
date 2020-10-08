import os
import smtplib
from email.message import EmailMessage
from assets.fileexplorer import fileExplorer
import filetype
from final import AI 
import pyautogui
import datetime
import time
import psutil
import pyjokes
import wikipedia
import webbrowser as wb


class Services(AI):
    # send email using google mail
    def mailService(self, subject, receiver, content):
        email_address = AI.db.email
        email_password = AI.db.emailpass

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = receiver
        msg.set_content(content)

        self.speak(('Do you want to attach a file?'))
        attachcontent = self.takeCommand()
        
        if attachcontent.lower() == 'yes':
            try:
                self.speak('How many files do you want to attach? ')
                attachcount = int(self.takeCommand())
                attachments = 0
                while attachments < attachcount:
                    file_path = fileExplorer()
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                        file_mime = filetype.guess_mime(f.name)
                        file_type = filetype.guess_extension(f.name)
                        file_name = f.name.split('/')[-1]
                    msg.add_attachment(file_data, maintype=file_mime, 
                    subtype=file_type, filename=file_name)
                    attachments += 1
            except ValueError:
                self.speak('You were meant to type a number.')
            except Exception as e:
                print(e)
        else:
            return 'Message will be sent without an attachment!'

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        self.speak('Your email has been sent!')
        return
        
    def clock(self):
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        self.speak(f"The current time is {Time}")
        return

    def date(self):
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        day = int(datetime.datetime.now().day)
        self.speak(f"The current date is {day}, {month}, {year}")
        return

    def screenshot(self):
        img = pyautogui.screenshot()
        img.save('C:\\projects\\AI\\screenshots\\ss.png')
        self.speak('Screenshot captured')
        return

    def cpu(self):
        usage = str(psutil.cpu_percent())
        battery = psutil.sensors_battery()
        self.speak(f'CPU is at {usage}')
        self.speak(f'Battery is at ' + {battery.percent})
        return
    
    def music(self):
        songs_dir = 'C:/Users/Michael/Music'
        files = os.listdir(songs_dir)
        songs = []
        for file in files:
            try:
                if filetype.is_audio(os.path.join(songs_dir, file)):
                    songs.append(file)
            except PermissionError:
                continue
        os.startfile(os.path.join(songs_dir, songs[0])) 
    
    def joke(self):
        self.speak(pyjokes.get_joke())
        return

    def wikisearch(self, query):
        AI().speak("Searching...")
        query = query.replace("search wikipedia for", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        self.speak(result)

    def chromesearch(self):
        self.speak('What should I search for?')
        chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        search = self.takeCommand().lower() 
        wb.get(chromepath).open_new_tab(search)

    def memory(self):
        
        return