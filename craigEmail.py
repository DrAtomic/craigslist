import pandas as pd
import csv, smtplib, ssl
from email.message import EmailMessage

def sendEmail(df,subject,body,sender,password):

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        server.login(sender, password)
        for email in df['email']:
            try:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = sender
                msg.set_content(body)
                msg['to'] = email
                server.send_message(msg)

            except smtplib.SMTPRecipientsRefused:
                pass


if __name__ == "__main__":
    df = pd.read_csv('file')
    subject = 'test'
    body = 'this is a test'
    sender = 'sender email here'
    password = 'password to sender email here'
    sendEmail(df,subject,body,sender,password)
    print('done')
