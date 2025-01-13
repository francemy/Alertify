from src.alerta_email import enviar_alerta_email

def test_envio_email():
    assert enviar_alerta_email("Teste", "Essa é uma mensagem de teste!") == True
