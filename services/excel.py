from openpyxl import Workbook
from datetime import datetime
import os
from database.banco import buscar_registros, marcar_exportados

def exportar_excel():
    registros = buscar_registros()

    if not registros:
        print("Nenhum registro encontrado.")
        return

    os.makedirs("exports", exist_ok=True)

    nome = datetime.now().strftime(
        "financeiro_%m_%Y.xlsx"
    )

    caminho = f"exports/{nome}"

    arquivo = Workbook()

    aba = arquivo.active
    aba.title = "Financeiro"

    aba.append([
        "ID",
        "Local",
        "Data",
        "Hora",
        "Valor",
        "Pagamento",
        "CNPJ"
    ])

    for registro in registros:
        aba.append(registro)

    arquivo.save(caminho)
    marcar_exportados()
    print(f"\nExcel criado: {caminho}")
    input("\nPressione ENTER para continuar...")