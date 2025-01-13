import pyodbc
from dotenv import load_dotenv
import os 

load_dotenv("../configs/.env") 

# Configurações de conexão
server = os.getenv("server")
database = os.getenv("database")
# username = os.getenv("name")
# password = os.getenv("password")


print([server,database])

def build_Database():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC DRIVER 17 for SQL server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            # f'UID={username};'
            # f'PWD={password}'
            f'Trusted_Connection=yes;'
        )
        print("Conexão bem suceddida")

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

        # cursor.execute("INSERT INTO AlertaLogs (mensagem) VALUES (?)",("test de conexão sql Server com Python",))
        # conn.commit()
        # print("Registro inserido com sucesso!")

        cursor.execute("SELECT * FROM AlertaLogs")
        for row in cursor.fetchall():
            print(row)
        return conn
    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None
