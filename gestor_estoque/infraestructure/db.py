import os
from django.db import connection, transaction

def executar_all(path, params=None):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f'O arquivo {path} não foi encontrado.')

        with open(path, 'r') as file:
            sql = file.read()

        with connection.cursor() as cursor:
            cursor.execute(sql, params or ())
        print("Operação SQL executada com sucesso!")
        transaction.commit()
    except Exception as e:
        print(f"Erro ao executar o comando SQL: {e}")
        transaction.rollback()

def executar_get(path, params=None):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f'O arquivo {path} não foi encontrado.')

        with open(path, 'r') as file:
            sql = file.read()

        with connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Erro ao executar a consulta SQL: {e}")
        return None