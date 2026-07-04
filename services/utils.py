import database
import services
import data
import os
from datetime import datetime

### MAIN.py

VERSAO = "0.1"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def encerrar():
    print("\n\nEncerrando...")
    input("\nPressione ENTER para continuar...")
    limpar()

def logo_main():
    limpar()
    print(f"""
+----------------------------------------------------------+
|                                                          |
| ░█░█░█▀█░█░░░█░░░█▀▀░▀█▀░░░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░ |
| ░█▄█░█▀█░█░░░█░░░█▀▀░░█░░░░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░ |
| ░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀ |
|                                                          |
+----------------------------------------------------------+
                          v{VERSAO}
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

### FINANCEIRO.py

def logo_register():
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