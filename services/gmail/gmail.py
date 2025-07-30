"""Gmail Automation Service"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def create_email(recipients: list[str]) -> str:
    """Create an email with an attachment and send it via Gmail."""

    with open('services/gmail/email_body.html', 'r', encoding='utf-8') as file:
        email_body = file.read()

    sender = os.getenv('GMAIL_SENDER')
    gmail_key = os.getenv('GMAIL_KEY')

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ', '.join(recipients)
    message['Subject'] = 'Manuais de digitação - Sistema Vector'
    message.attach(MIMEText(email_body, 'html'))

    file_paths = [
        'static/files/Manuais.pdf',
        'static/files/Tutorial.mp4'
    ]
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), Name=os.path.basename(file_path))
            attachment['Content-Disposition'] = f'attachment; filename="{
                os.path.basename(file_path)}"'
            message.attach(attachment)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, gmail_key)
        server.send_message(message)

    return 'Email com anexo enviado com sucesso!'
