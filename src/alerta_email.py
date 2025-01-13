import smtplib
import os

def enviar_alerta_email(assunto, mensagem):
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    destinatario = "destinatario@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_user, email_password)
        mensagem_final = f"Subject: {assunto}\n\n{mensagem}"
        server.sendmail(email_user, destinatario, mensagem_final)
