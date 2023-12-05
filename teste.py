import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


db_user = os.getenv("POSTGRES_USER")
if db_user is None:
    print("Variável POSTGRES_USER não encontrada.")