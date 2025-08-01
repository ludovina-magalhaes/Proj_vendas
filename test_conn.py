import psycopg2
import sys

try:
    conn = psycopg2.connect(
        dbname="dbname_oici",
        user="dbname_oici_user",
        password="t6riKWrMWQiEwmG5ID9hnZMWNxfZcpKs",
        host="dpg-d1gohn2li9vc73auk1u0-a.oregon-postgres.render.com",
        port=5432,
        connect_timeout=10
    )
    print(" Conectado com sucesso!")
    conn.close()
except Exception as e:
    print(" Erro na conexão:", e)
    sys.exit(1)


### Cria um script query_postgres.py

import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

print("Diretório atual:", os.getcwd())  # Mostra o diretório onde o script está rodando

# ---------- CARREGAR VARIÁVEIS DE AMBIENTE ----------
load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

# ---------- CONEXÃO COM O POSTGRES ----------
def conectar_postgresql(user, password, host, port, database):
    url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(url)
    return engine

# ---------- EXECUTAR CONSULTA ----------
def executar_consulta(engine, query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

def ler_query_de_arquivo(caminho_arquivo):
    caminho_absoluto = os.path.abspath(caminho_arquivo)
    print(f"Tentando abrir o arquivo em: {caminho_absoluto}")
    with open(caminho_absoluto, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    print(f"Conteúdo do ficheiro lido (primeiros 200 caracteres):\n{conteudo[:200]}")
    return conteudo

if __name__ == "__main__":
    engine = conectar_postgresql(user, password, host, port, database)

    # Teste rápido com consulta direta
    query_teste = 'SELECT * FROM "Superstore_dados_limpos" LIMIT 5;'
    df_teste = executar_consulta(engine, query_teste)
    print(df_teste)

    # Consulta via ficheiro .sql
    caminho_query = '../consultas_vendas.sql'  # Ajuste o caminho conforme sua estrutura
    query = ler_query_de_arquivo(caminho_query)

    if not query.strip():
        print("Erro: A query está vazia!")
    else:
        df = executar_consulta(engine, query)
        print(df)
