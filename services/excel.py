from openpyxl import Workbook
from datetime import datetime
import os
from database import banco

def exportar_excel():
    entrada = banco.entradas_pendentes()
    despesa = banco.despesas_pendentes()

    if not entrada and not despesa:
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

    aba_entrada = arquivo.active
    aba_entrada.title = "Entradas"

    aba_entrada.append([
        "ID",
        "Valor",
        "Pagamento",
        "Banco",
        "Origem",
        "Data",
        "Hora",
        "Remetente"
    ])

    for registro in entrada:
        aba_entrada.append(registro)

    aba_despesa = arquivo.create_sheet("Despesas")

    aba_despesa.append([
        "ID",
        "Valor",
        "Pagamento",
        "Banco",
        "Local",
        "Data",
        "Hora",
        "CNPJ"
    ])

    for registro in despesa:
        aba_despesa.append(registro)

    arquivo.save(caminho)

    banco.marcar_entradas_exportadas()
    banco.marcar_despesas_exportadas()

    banco.limpar_registros()
    
    print(f"\nExcel criado: {caminho}")
    input("\nPressione ENTER para continuar...")