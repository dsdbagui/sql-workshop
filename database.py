from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


db_user = os.getenv("POSTGRES_USER")
if db_user is None:
    print("Variável POSTGRES_USER não encontrada.")
db_password = os.getenv("POSTGRES_PASSWORD")
if db_password is None:
    print("Variável POSTGRES_PASSWORD não encontrada.")
db_name = os.getenv("POSTGRES_DB")
if db_name is None:
    print("Variável POSTGRES_DB não encontrada.")
db_host = os.getenv("DB_HOST")
if db_host is None:
    print("Variável DB_HOST não encontrada.")
db_port = os.getenv("DB_PORT")
if db_port is None:
    print("Variável DB_PORT não encontrada.")

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando a engine de conexão
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)

# Criando a sessão

Session = sessionmaker(bind=engine)

Base = declarative_base()


# Definindo o modelo de dados
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)


# Criando a tabela
Base.metadata.create_all(bind=engine)