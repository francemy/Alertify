Aqui está uma sugestão de descrição para o seu projeto de automação de alertas:

---

### **Alertify: Sistema de Automação de Monitoramento e Alerta**

**Alertify** é uma solução de automação desenvolvida para monitorar a conectividade de servidores e redes, enviando alertas em tempo real quando problemas de rede são detectados. Com o uso de **ping** para verificar a disponibilidade de servidores externos, o sistema garante a detecção precoce de falhas, mantendo os responsáveis informados através de notificações por email ou SMS.

#### **Funcionalidades principais:**
- **Monitoramento contínuo:** O sistema realiza verificações periódicas de conectividade com servidores e IPs remotos.
- **Alertas automáticos:** Em caso de falhas de conexão, alertas são enviados automaticamente por **email** e **SMS**.
- **Registro de logs:** Todos os eventos, tanto de sucesso quanto falha, são registrados em um banco de dados SQL para posterior análise.
- **Tarefa automatizada:** Realização de tarefas pré-configuradas, como o envio de alertas periódicos, garantindo que todos os problemas sejam rapidamente detectados.

#### **Tecnologias usadas:**
- **Python:** Linguagem de programação principal para a automação.
- **pyodbc:** Conexão com o banco de dados SQL Server.
- **schedule:** Agendamento de tarefas para garantir a execução contínua do monitoramento.
- **subprocess:** Utilizado para executar comandos de **ping** e verificar a conectividade de servidores.
# Automação de Alerta em Python

Este projeto visa automatizar o processo de monitoramento e envio de alertas, integrando com um banco de dados SQL Server para registrar os logs. A automação envolve monitoramento de rede e envio de alertas via e-mail ou SMS em caso de falhas.

## Funcionalidades

- **Monitoramento de Rede**: Verifica a conectividade com um servidor externo (por exemplo, `8.8.8.8`) usando o comando `ping`.
- **Envio de Alertas**: Envia alertas via e-mail e SMS quando a conectividade do servidor é perdida.
- **Registro de Logs**: Armazena informações sobre falhas e sucesso de monitoramento no banco de dados SQL Server.

## Pré-requisitos

Antes de rodar o projeto, é necessário configurar o ambiente e instalar as dependências:

- Python 3.6 ou superior
- Pacotes Python: `pyodbc`, `dotenv`, `schedule`, `subprocess`, entre outros.
- Banco de Dados SQL Server (configurável via variáveis de ambiente).

## Como Usar

### 1. **Instalação**

Clone o repositório ou baixe os arquivos do projeto.

```bash
git clone [https://github.com/seu-usuario/automacao-alerta-python.git](https://github.com/francemy/Alertify.git)
cd automacao-alerta-python
```

### 2. **Configuração do Ambiente**

Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis de ambiente:

```env
server=SEU_SERVIDOR
database=SEU_BANCO_DE_DADOS
```

### 3. **Instalação das Dependências**

Instale as dependências necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter as bibliotecas necessárias:

```txt
pyodbc
dotenv
schedule
```

### 4. **Configuração do Banco de Dados**

O script conecta-se ao SQL Server e cria uma tabela de logs chamada `AlertaLogs` caso ela não exista. A tabela irá armazenar mensagens de alerta e a data/hora do registro.

### 5. **Executando o Script**

Para iniciar o monitoramento e a automação de alertas, execute o seguinte script:

```bash
python monitoramento_alerta.py
```

### 6. **Monitoramento e Alerta**

O script realiza um ping a cada minuto para o servidor `8.8.8.8`. Caso o servidor esteja fora do ar, um alerta será enviado e registrado no banco de dados. Caso contrário, um alerta informando que o servidor está funcionando corretamente também será registrado.

## Código do Projeto

### Função de Conexão ao Banco de Dados (`build_Database`)

A função `build_Database` conecta-se ao banco de dados SQL Server e cria a tabela `AlertaLogs` para armazenar os logs.

```python
def build_Database():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC DRIVER 17 for SQL server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'
        )
        print("Conexão bem sucedida")

        cursor = conn.cursor()
        cursor.execute('''
        IF OBJECT_ID('AlertaLogs', 'U') IS NULL
        BEGIN
        CREATE TABLE AlertaLogs (
            id INT PRIMARY KEY IDENTITY(1,1),
            mensagem NVARCHAR(255),
            data_hora DATETIME DEFAULT GETDATE()
        )
        END
        ''')
        conn.commit()
        print("Tabela criada com sucesso!")

        cursor.execute("SELECT * FROM AlertaLogs")
        for row in cursor.fetchall():
            print(row)
        return conn
    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None
```

### Função de Monitoramento de Rede

A função `monitor_network` verifica a conectividade com o servidor utilizando `ping` e registra o resultado no banco de dados.

```python
def monitor_network():
    host = "8.8.8.8"
    print(f'{host} servidor de teste')
    if not ping_server(host):
        mensagem_erro = f"ALERTA: o servidor {host} está fora do ar!"
        send_alert(mensagem_erro)  # Enviar alerta
        registrar_log(mensagem_erro)  # Registrar o log no banco de dados
    else :
        mensagem_erro = f"Boa: o servidor {host} está funcionando corretamente!"
        send_alert(mensagem_erro)  # Enviar alerta
        registrar_log(mensagem_erro)  # Registrar o log no banco de dados
```

### Agendamento de Tarefas

A tarefa de monitoramento é agendada para rodar a cada minuto utilizando a biblioteca `schedule`.

```python
schedule.every(1).minutes.do(monitor_network)
```

### Loop de Execução

O loop contínuo mantém a automação rodando, verificando periodicamente a conectividade do servidor.

```python
while True:
    schedule.run_pending()
    time.sleep(1)
```

## Contribuindo

Se você quiser contribuir para o projeto, fique à vontade para fazer um fork e enviar pull requests. 

### 1. Fork o repositório
### 2. Crie uma branch para sua feature
### 3. Comite suas alterações
### 4. Envie um pull request

## Licença

Este projeto é licenciado sob a python e twilio.

