import database
import services
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

### DESPESA.py

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

def listar_pendentes():

    registros = database.banco.registros_pendentes()

    if not registros:
        print("\nNenhum registro pendente.")
        input("\nENTER para continuar...")
        return

    logo_main()

    print("""============================
 REGISTROS NÃO EXPORTADOS
============================""")

    for registro in registros:

        tipo = registro[1]

        if tipo.lower() == "entrada":
            cor = "\033[92m"      # verde
        else:
            cor = "\033[91m"      # vermelho

        print(f"""
{cor}ID\033[0m: {registro[0]}

{cor}Tipo\033[0m: {registro[1]}
{cor}Valor\033[0m: R$ {registro[2]:.2f}
{cor}Forma\033[0m: {registro[3]}
{cor}Banco\033[0m: {registro[4]}
{cor}Contraparte\033[0m: {registro[5]}
{cor}Data\033[0m: {registro[6]}
{cor}Hora\033[0m: {registro[7]}
----------------------------""")

    input("\nENTER para continuar...")

def gerar_nome_unico(pasta, nome_base, extensao):
    nome = f"{nome_base}.{extensao}"
    contador = 2

    while os.path.exists(os.path.join(pasta, nome)):
        nome = f"{nome_base} ({contador}).{extensao}"
        contador += 1

    return os.path.join(pasta, nome)