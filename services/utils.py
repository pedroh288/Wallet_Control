import database
import services
import os
from datetime import datetime

cor_entrada = "\033[92m"
cor_despesa = "\033[91m"
cor_ciano = "\033[36m"
cor_ciano_claro = "\033[1;96m"

cor_reset = "\033[0m"

### MAIN.py

VERSAO = "0.2"

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

    print(f"""\n{cor_ciano}Banco{cor_reset} utilizado:
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

    entradas = database.banco.entradas_pendentes()
    despesas = database.banco.despesas_pendentes()

    if not entradas and not despesas:
        print("\nNenhum registro pendente.")
        input("\nENTER para continuar...")
        return

    logo_main()

    print(f"""============================
 {cor_ciano_claro}REGISTROS NÃO EXPORTADOS{cor_reset}
============================""")

# ENTRADA

    for registro in entradas:

        print(f"""
{cor_entrada}ID{cor_reset}: {registro[0]}

{cor_entrada}Tipo{cor_reset}: Entrada
{cor_entrada}Valor{cor_reset}: R$ {registro[1]:.2f}
{cor_entrada}Forma{cor_reset}: {registro[2]}
{cor_entrada}Banco{cor_reset}: {registro[3]}
{cor_entrada}Origem{cor_reset}: {registro[4]}
{cor_entrada}Data{cor_reset}: {registro[5]}
{cor_entrada}Hora{cor_reset}: {registro[6]}
{cor_entrada}Remetente{cor_reset}: {registro[7]}
----------------------------""")

# DESPESA

    for registro in despesas:

        print(f"""
{cor_despesa}ID{cor_reset}: {registro[0]}

{cor_despesa}Tipo{cor_reset}: Despesa
{cor_despesa}Valor{cor_reset}: R$ {registro[1]:.2f}
{cor_despesa}Forma{cor_reset}: {registro[2]}
{cor_despesa}Banco{cor_reset}: {registro[3]}
{cor_despesa}Local{cor_reset}: {registro[4]}
{cor_despesa}Data{cor_reset}: {registro[5]}
{cor_despesa}Hora{cor_reset}: {registro[6]}
{cor_despesa}CNPJ{cor_reset}: {registro[7]}
----------------------------""")

    input("\nENTER para continuar...")

def gerar_nome_unico(pasta, nome_base, extensao):
    nome = f"{nome_base}.{extensao}"
    contador = 2

    while os.path.exists(os.path.join(pasta, nome)):
        nome = f"{nome_base} ({contador}).{extensao}"
        contador += 1

    return os.path.join(pasta, nome)