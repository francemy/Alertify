import schedule
import time
import subprocess
from alerta_email import enviar_alerta_email
from alerta_sms import send_alert
from ConectDB import build_Database

# Função para registrar log no banco de dados
def registrar_log(mensagem):
    db = build_Database()
    if db: 
        cursor = db.cursor()
        cursor.execute("INSERT INTO AlertaLogs (mensagem) VALUES (?)", (mensagem,))
        db.commit()
        db.close()  # Fechar a conexão corretamente

# Função de tarefa automatizada
def tarefa_automatica():
    enviar_alerta_email("Teste de automação", "Esse é um alerta automático!")

# Função para realizar o ping em um host
def ping_server(host):
    try:
        output = subprocess.check_output(["ping", "-n", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False

# Função para monitorar a rede
def monitor_network():
    host = "8.8.8.8"
    print(f'{host} servidor de test')
    if not ping_server(host):
        mensagem_erro = f"ALERTA: o servidor {host} está fora do ar!"
        send_alert(mensagem_erro)  # Enviar alerta
        registrar_log(mensagem_erro)  # Registrar o log no banco de dados
    else :
        mensagem_erro = f"Boa: o servidor {host} está funcionando correctamente!"
        send_alert(mensagem_erro)  # Enviar alerta
        registrar_log(mensagem_erro)  # Registrar o log no banco de dados
        

# Agendar a tarefa para rodar a cada minuto
schedule.every(1).minutes.do(monitor_network)

# Loop contínuo para manter a automação rodando
while True:
    schedule.run_pending()
    time.sleep(1)

