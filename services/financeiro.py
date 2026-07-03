import os
import database
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    limpar()
    print("""····························································
:                                                          :
:  _ _               ___            _        _             :
: | \ | ___  _ _ _  | . \ ___  ___ <_> ___ _| |_ ___  _ _  :
: |   |/ ._>| | | | |   // ._>/ . || |<_-<  | | / ._>| '_> :
: |_\_|\___.|__/_/  |_\_\\___.\_. ||_|/__/  |_| \___.|_|   :
:                             <___'                        :
:                                                          :
····························································
""")

def pedir_data(mensagem):

    while True:
        data = input(mensagem).strip()

        if data == "":
            return "Não informado"

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida! Use DD/MM/YYYY")

def pedir_hora(mensagem):

    while True:
        hora = input(mensagem).strip()

        if hora == "":
            return "Não informado"

        try:
            datetime.strptime(hora, "%H:%M")
            return hora

        except ValueError:
            print("Data inválida! Use HH:MM")

def pedir_valor(mensagem):

    while True:
        valor = input(mensagem).strip()

        try:
            valor = float(valor.replace(",", "."))
            return valor

        except ValueError:
            print("Digite um valor válido!")
    
def pedir_banco():

    bancos = {
        "1": "Banco do Brasil",
        "2": "Bradesco",
        "3": "Caixa",
        "4": "Inter",
        "5": "Itaú",
        "6": "Nubank",
        "7": "Santander",
        "8": "Outro",
        "0": "Não informado"
    }

    print("""
Banco utilizado:
[1] Banco do Brasil
[2] Bradesco
[3] Caixa
[4] Inter
[5] Itaú
[6] Nubank
[7] Santander
[8] Outro
[0] Não informado
""")

    while True:

        escolha = input("\nEscolha: ").strip()

        if escolha in bancos:

            if escolha == "8":
                return input("Nome do banco: ").strip()

            return bancos[escolha]

        print("Digite apenas um número correspondente!")

def novo_registro():
    try:
        logo()
        print("\n=== Novo Registro ===".upper())
        valor = pedir_valor("\nValor (R$): ")

        print("""\nForma de pagamento:
[1] PIX
[2] Dinheiro
[3] Débito
[4] Crédito
[5] Boleto
[0] Não informar""")

        formas = {
            "1": "PIX",
            "2": "Dinheiro",
            "3": "Débito",
            "4": "Crédito",
            "5": "Boleto",
            "0": "Não informado"
        }

        while True:
            pagamento = input("\nEscolha: ").strip()
        
            if pagamento in formas:
                pagamento = formas[pagamento]

                if pagamento in ("PIX", "Débito", "Crédito"):
                    bancos = pedir_banco()

                else:
                    bancos = "Não se aplica"
                break

            print("Digite apenas o número correpondente!")
        
        local = input("\nLocal: ").strip()

        if local == "":
            local = "Não informado"

        data = pedir_data ("\nData (DD/MM/AAAA): ")
        hora = pedir_hora("\nHora (HH:MM): ")
        
        while True:
            cnpj = input("\nCNPJ: ").strip()

            if cnpj.isdigit():
                break
            if cnpj == "":
                cnpj = "Não informado"
                break
        
        print ("CNPJ deve conter apenas números!")
        
        registro = {

            "valor": f"R$ {valor}",
            "pagamento": pagamento,
            "banco": bancos,
            "local": local,
            "data": data,
            "hora": hora,
            "cnpj": cnpj
        }

        database.banco.salvar_registro(registro)
        
        print("""============================
      REGISTRO CRIADO
============================
    """)
        
        for chave, valor in registro.items():
            print(f"{chave.capitalize()}: {valor}")
        input("\nPressione ENTER para continuar...")
        return True
    
    except (KeyboardInterrupt, EOFError):
        print("\n\nVoltando ao menu...")
        input("\nPressione ENTER para continuar...")
        return None

def listar_pendentes():

    registros = database.banco.registros_pendentes()

    if not registros:

        print("\nNenhum registro pendente.")
        input("\nENTER para continuar...")
        return

    print("""============================
 REGISTROS NÃO EXPORTADOS
============================""")
    for registro in registros:
        print(f"""
ID: {registro[0]}
Valor: R$ {registro[1]}
Pagamento: {registro[2]}
Banco {registro[3]}
Local: {registro[4]}
Data: {registro[5]}
Hora: {registro[6]}
CNPJ: {registro[7]}
----------------------------
""")

    input("ENTER para continuar...")

if __name__ == "__main__":
    novo_registro()