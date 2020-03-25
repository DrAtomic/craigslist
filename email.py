#!/usr/bin/env python3

import pandas as pd
import csv, smtplib, ssl
from email.message import EmailMessage

def email(df,subject,body,sender,password):

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        server.login(from_address, password)
        try:
            for email in df['email']:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = sender
                msg.set_content(body)
                msg['to'] = email
                server.send_message(msg)
        except:
            pass

if __name__ == "__main__":
    df = pd.read_csv('file')
    subject = 'test'
    body = 'this is a test'
    sender = 'sender email here'
    password = 'password to sender email here'
    email(df,subject,body,sender,password)
    print('done')
