from twilio.rest import Client

# Substitua pelos seus dados do Twilio
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Usar a chave do Twilio de uma variável de ambiente
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# envia a mensagem
client = Client (twilio_account_sid, twilio_auth_token)


def send_alert(mensage):
    message= client.messages.create(
        body=mensage,
        from_=os.getenv("twilio_number"),
        to=os.getenv("destinatario_number")
    )

# print(f"mensagen enviada com sucesso SID: {message.sid}")