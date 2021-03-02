#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import ssl

def generate(sender, recipient, subject, body):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message

def send(message, server, port, login, password):
    """Sends the message to the configured SMTP server."""
    
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(login, password)
            server.set_debuglevel(1)
            server.send_message(message)
            server.quit()
    except Exception as e:
        raise e
