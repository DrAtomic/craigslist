#!/usr/bin/env python3

#ya9jABCgFtMnAj8
#password
#email
#Lucas Maloney
#lucas.alan.maloney@gmail.com

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "lucas.alan.maloney@gmail.com"  # Enter your address
receiver_email = "leo.ward.garcia@gmail.com"  # Enter receiver address
password = ya9jABCgFtMnAj8
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
