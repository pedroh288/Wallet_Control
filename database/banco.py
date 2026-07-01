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

        Valor TEXT,
        Pagamento TEXT,
        Local TEXT,
        Data TEXT,
        Hora TEXT,
        CNPJ TEXT,

        exportado INTEGER DEFAULT 0
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
        valor,
        pagamento,
        local,
        data,
        hora,
        cnpj
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        registro["valor"],
        registro["pagamento"],
        registro["local"],
        registro["data"],
        registro["hora"],
        registro["cnpj"]
    ))

    conexao.commit()
    conexao.close()

def buscar_registros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        pagamento,
        local,
        data,
        hora,
        cnpj
    FROM pagamentos
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def registros_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id,
        valor,
        pagamento,
        local,
        data,
        hora,
        cnpj
    FROM pagamentos
    WHERE exportado = 0
    """)

    registros = cursor.fetchall()
    conexao.close()

    return registros

def marcar_exportados():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE pagamentos
    SET exportado = 1
    WHERE exportado = 0
    """)

    conexao.commit()
    conexao.close()