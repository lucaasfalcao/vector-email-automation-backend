"""Gmail Automation Service"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def create_email(destinatario: str) -> str:
    """Create an email with an attachment and send it via Gmail."""

    # corpo do email (em HTML)
    with open('services/gmail/email_body.html', 'r', encoding='utf-8') as file:
        corpo_email = file.read()

    # dados do email
    remetente = 'lucaasfalcao999@gmail.com'
    #nayara@vectorfidc.com.br
    senha_app = 'brtn miff npds cnej' # MUDAR PARA ENV!!

    # configurar a mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = 'Manuais de digitação - Sistema Vector'
    mensagem.attach(MIMEText(corpo_email, 'html'))

    # anexo
    caminho_arquivo = 'static/files/Manuais.pdf'
    with open(caminho_arquivo, 'rb') as file:
        anexo = MIMEApplication(file.read(), Name=os.path.basename(caminho_arquivo))
        anexo['Content-Disposition'] = f'attachment; filename="{os.path.basename(caminho_arquivo)}"'
        mensagem.attach(anexo)

    # enviar o e-mail via Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha_app)
        servidor.send_message(mensagem)

    return 'Email com anexo enviado com sucesso!'
