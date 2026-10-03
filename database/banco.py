import os
import sys
import sqlite3

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CAMINHO = os.path.join(DATA_DIR, "financeiro.db")

def conectar():
    return sqlite3.connect(CAMINHO)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Entradas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        Valor REAL,
        Forma_Pagamento TEXT,
        Banco TEXT,
        Origem TEXT,
        Data TEXT,
        Hora TEXT,
        Remetente TEXT,

        exportado INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Despesas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        Valor REAL,
        Forma_Pagamento TEXT,
        Banco TEXT,
        Local TEXT,
        Data TEXT,
        Hora TEXT,
        Remetente TEXT,
        CNPJ TEXT,

        exportado INTEGER DEFAULT 0
    )
    """)

    conexao.commit()
    conexao.close()

def salvar_entrada(registro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO entradas
    (
        valor,
        forma_pagamento,
        banco,
        origem,
        data,
        hora,
        remetente
    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """,
    (
        registro["valor"],
        registro["forma_pagamento"],
        registro["banco"],
        registro["origem"],
        registro["data"],
        registro["hora"],
        registro["remetente"]
    ))

    conexao.commit()
    conexao.close()

def salvar_despesa(registro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO despesas
    (
        valor,
        forma_pagamento,
        banco,
        local,
        data,
        hora,
        cnpj
    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """,
    (
        registro["valor"],
        registro["forma_pagamento"],
        registro["banco"],
        registro["local"],
        registro["data"],
        registro["hora"],
        registro["cnpj"]
    ))

    conexao.commit()
    conexao.close()

def buscar_entradas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        forma_pagamento,
        banco,
        origem,
        data,
        hora,
        remetente
    FROM entradas
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def buscar_despesas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        forma_pagamento,
        banco,
        local,
        data,
        hora,
        cnpj
    FROM despesas
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def entradas_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        forma_pagamento,
        banco,
        origem,
        data,
        hora,
        remetente
    FROM entradas
    WHERE exportado = 0
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def despesas_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        forma_pagamento,
        banco,
        local,
        data,
        hora,
        cnpj
    FROM despesas
    WHERE exportado = 0
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def marcar_entradas_exportadas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE entradas
    SET exportado = 1
    WHERE exportado = 0
    """)

    conexao.commit()
    conexao.close()

def marcar_despesas_exportadas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE despesas
    SET exportado = 1
    WHERE exportado = 0
    """)

    conexao.commit()
    conexao.close()

def limpar_registros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM entradas")
    cursor.execute("DELETE FROM despesas")

    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Entradas'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Despesas'")

    conexao.commit()
    conexao.close()