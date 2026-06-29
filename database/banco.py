import sqlite3

CAMINHO = "data/financeiro.db"

def conectar():
    return sqlite3.connect(CAMINHO)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamentos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        local TEXT,
        data TEXT,
        hora TEXT,
        valor TEXT,
        pagamento TEXT,
        cnpj TEXT

    )
    """)

    conexao.commit()
    conexao.close()

def salvar_registro(registro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO pagamentos
    (
        local,
        data,
        hora,
        valor,
        pagamento,
        cnpj
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        registro["local"],
        registro["data"],
        registro["hora"],
        registro["valor"],
        registro["pagamento"],
        registro["cnpj"]
    ))

    conexao.commit()
    conexao.close()

def buscar_registros():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM pagamentos
    """)

    registros = cursor.fetchall()

    conexao.close()

    return registros