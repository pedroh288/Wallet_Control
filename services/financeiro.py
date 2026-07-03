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

    banco = {
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
\033[36mBanco\033[0m utilizado:
[1] Banco do Brasil
[2] Bradesco
[3] Caixa
[4] Inter
[5] Itaú
[6] Nubank
[7] Santander
[8] Outro
[0] Não informado""")

    while True:

        escolha = input("\nEscolha: ").strip()

        if escolha in banco:

            if escolha == "8":
                return input("Nome do banco: ").strip()

            return banco[escolha]

        print("Digite apenas um número correspondente!")
        print("---------------")

def novo_registro():
    try:
        logo()
        print("\n=== Novo Registro ===".upper())
        valor = pedir_valor("\n\033[36mValor\033[0m (R$): ")
        print("---------------")

        print("""\nForma de \033[36mPagamento\033[0m:
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
                print("---------------")

                if pagamento in ("PIX", "Débito", "Crédito"):
                    banco = pedir_banco()
                    print("---------------")

                else:
                    banco = "Não se aplica"
                break

            print("Digite apenas o número correpondente!")
        
        local = input("\n\033[36mLocal\033[0m: ").strip()

        if local == "":
            local = "Não informado"
        print("---------------")

        data = pedir_data ("\n\033[36mData\033[0m (DD/MM/AAAA): ")
        print("---------------")
        hora = pedir_hora("\n\033[36mHora\033[0m (HH:MM): ")
        print("---------------")
        
        while True:
            cnpj = input("\n\033[36mCNPJ\033[0m: ").strip()

            if cnpj.isdigit():
                break
            if cnpj == "":
                cnpj = "Não informado"
                break
        
            print ("CNPJ deve conter apenas números!")
        print("---------------")
        
        registro = {
            "valor": valor,
            "pagamento": pagamento,
            "banco": banco,
            "local": local,
            "data": data,
            "hora": hora,
            "cnpj": cnpj
        }

        database.banco.salvar_registro(registro)
        
        print("""
============================
      REGISTRO CRIADO
============================
""")
        
        for chave, valor in registro.items():

            if chave == "valor":
                print(f"\033[91mValor\033[0m: R$ {valor:.2f}")
            elif chave == "cnpj":
                print(f"\033[91mCNPJ\033[0m: {cnpj}")
            else:
                print(f"\033[91m{chave.capitalize()}\033[0m: {valor}")

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
 REGISTROS \033[41mNÃO\33[0m EXPORTADOS
============================""")
    for registro in registros:
        print(f"""
\033[91mID\033[0m: {registro[0]}

\033[91mValor\033[0m: R$ {registro[1]:.2f}
\033[91mPagamento\033[0m: {registro[2]}
\033[91mBanco\033[0m: {registro[3]}
\033[91mLocal\033[0m: {registro[4]}
\033[91mData\033[0m: {registro[5]}
\033[91mHora\033[0m: {registro[6]}
\033[91mCNPJ\033[0m: {registro[7]}
----------------------------""")

    input("\nENTER para continuar...")

if __name__ == "__main__":
    novo_registro()