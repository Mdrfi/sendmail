# Mehrshad Raoufi 
# 9811281412
import smtplib, ssl 
import os 
import pickle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# def readauth():
#     with open('Pickle Path', 'rb') as file:
#         auth = pickle.load(file)
#         mail = auth['mail']
#         password = auth['pass']
#     return mail, password

def send_email():
    # mail, password = readauth()
    mail = input('Pleaae enter your gamil...  ')
    password = input('please enter your password...  ')
    port = 465
    context = ssl.create_default_context()
    # recieve = 'mehrshadraoufi@gmail.com'
    recieve = input('Please enter destination email...  ')
    message = MIMEMultipart('alternative')
    msg = f""" <p style="font-size:26px; color: #222222"> {input('Please enter your message...  ')} </p>
    <a href="https://mdrfi.net" style="color: #ffd600"> Mdrfi </a>
    """
    message['From'] = mail
    message['To'] = recieve
    message['Subject'] = 'Send email from python'

    message.attach(MIMEText(msg, "html"))

    with smtplib.SMTP_SSL('smtp.gmail.com', port,context=context) as server:
        server.login(mail, password)
        server.sendmail(mail, recieve, message.as_string())
    print('Misson Pass')


if __name__ == '__main__':
    send_email()
 
