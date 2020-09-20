import os
import smtplib
from email.message import EmailMessage
from fileexplorer import fileExplorer
import filetype


def mailService(subject, receiver, content):
    email_address = os.environ.get('EMAIL_USER')
    email_password = os.environ.get('EMAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = receiver
    msg.set_content(content)

    attachcontent = input('Do you want to attach a file?(Yes/No): ')
    
    if attachcontent.lower() == 'yes':
        try:
            attachcount = int(input('How many files do you want to attach? '))
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
            print('You were meant to type a number.')
        except Exception as e:
            print(e)
    else:
        return 'Message will be sent without an attachment!'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
    return
