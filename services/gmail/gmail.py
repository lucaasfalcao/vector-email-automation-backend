"""Gmail Automation Service"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def create_email(recipient: str) -> str:
    """Create an email with an attachment and send it via Gmail."""

    with open('services/gmail/email_body.html', 'r', encoding='utf-8') as file:
        corpo_email = file.read()

    sender = os.getenv('GMAIL_SENDER')
    gmail_key = os.getenv('GMAIL_KEY')

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Manuais de digitação - Sistema Vector'
    message.attach(MIMEText(corpo_email, 'html'))

    caminho_arquivo = 'static/files/Manuais.pdf'
    with open(caminho_arquivo, 'rb') as file:
        anexo = MIMEApplication(file.read(), Name=os.path.basename(caminho_arquivo))
        anexo['Content-Disposition'] = f'attachment; filename="{os.path.basename(caminho_arquivo)}"'
        message.attach(anexo)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, gmail_key)
        server.send_message(message)

    return 'Email com anexo enviado com sucesso!'
