from openpyxl import Workbook
from datetime import datetime
import os
from database import banco

def exportar_excel():
    registros = banco.buscar_registros()

    if not registros:
        print("Nenhum registro encontrado.")
        return

    os.makedirs("exports", exist_ok=True)

    base = datetime.now().strftime("financeiro_%m_%Y")
    nome = f"{base}.xlsx"

    contador = 2

    while os.path.exists(os.path.join("exports", nome)):
        nome = f"{base} ({contador}).xlsx"
        contador += 1

    caminho = os.path.join("exports", nome)

    arquivo = Workbook()

    aba = arquivo.active
    aba.title = "Financeiro"

    aba.append([
        "ID",
        "Tipo",
        "Valor",
        "Pagamento",
        "Banco",
        "Contraparte",
        "Data",
        "Hora"
    ])

    for registro in registros:
        aba.append(registro)

    arquivo.save(caminho)
    banco.marcar_exportados()
    banco.limpar_registros()
    print(f"\nExcel criado: {caminho}")
    input("\nPressione ENTER para continuar...")