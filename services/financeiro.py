import os
from database.banco import salvar_registro
from database.banco import registros_pendentes

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    limpar()
    print("""
····························································
:                                                          :
:  _ _               ___            _        _             :
: | \ | ___  _ _ _  | . \ ___  ___ <_> ___ _| |_ ___  _ _  :
: |   |/ ._>| | | | |   // ._>/ . || |<_-<  | | / ._>| '_> :
: |_\_|\___.|__/_/  |_\_\\___.\_. ||_|/__/  |_| \___.|_|   :
:                             <___'                        :
:                                                          :
····························································
""")
    
def novo_registro():
    try:
        logo()
        print("\n=== Novo Registro ===".upper())
        local = input("\nLocal: ").strip()
        data = input("\nData (DD/MM/AAAA): ").strip()
        hora = input("\nHora (HH:MM): ").strip()
        valor = input("\nValor (R$): ").strip()
        print("""\nForma de pagamento:
[1] PIX
[2] Dinheiro
[3] Débito
[4] Crédito""")
        
        pagamento = input("Escolha: ").strip()
        formas = {
            "1": "PIX",
            "2": "Dinheiro",
            "3": "Débito",
            "4": "Crédito"
        }
        pagamento = formas.get(pagamento, "Não informado")
        cnpj = input("\nCNPJ (opcional): ").strip()

        if cnpj == "":
            cnpj = "Não informado"
        
        registro = {
            "local": local,
            "data": data,
            "hora": hora,
            "valor": valor,
            "pagamento": pagamento,
            "cnpj": cnpj
        }

        salvar_registro(registro)
        
        print("""
============================
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

    registros = registros_pendentes()

    if not registros:

        print("\nNenhum registro pendente.")
        input("\nENTER para continuar...")
        return


    print("""
============================
 REGISTROS NÃO EXPORTADOS
============================
""")


    for registro in registros:

        print(f"""
ID: {registro[0]}
Local: {registro[1]}
Data: {registro[2]}
Hora: {registro[3]}
Valor: R${registro[4]}
Pagamento: {registro[5]}
CNPJ: {registro[6]}
----------------------------
""")


    input("ENTER para continuar...")

if __name__ == "__main__":
    novo_registro()