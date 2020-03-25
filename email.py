#!/usr/bin/env python3


import csv, smtplib, ssl

message = """Subject: subject here
message here
"""
from_address = "email here"
password = 'password here'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("dataWithEmail.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for email in reader:
            try:
                server.sendmail(
                    from_address,
                    email,
                    message)
            except:
                pass

