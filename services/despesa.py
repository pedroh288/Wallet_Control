import database
from datetime import datetime
import services

def despesa_registro():
    try:
        services.utils.logo_register()
        print("\n=== Novo Registro ===".upper())
        valor = services.utils.pedir_valor("\n\033[36mValor\033[0m (R$): ")
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
                    banco = services.utils.pedir_banco()
                    print("---------------")

                else:
                    banco = "Não se aplica"
                break

            print("Digite apenas o número correpondente!")
        
        local = input("\n\033[36mLocal\033[0m: ").strip()

        if local == "":
            local = "Não informado"
        print("---------------")

        data = services.utils.pedir_data ("\n\033[36mData\033[0m (DD/MM/AAAA): ")
        print("---------------")
        hora = services.utils.pedir_hora("\n\033[36mHora\033[0m (HH:MM): ")
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
            "tipo":"Depesa",
            "valor": valor,
            "forma_pagamento": pagamento,
            "banco": banco,
            "contraparte": local,
            "data": data,
            "hora": hora
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
            elif chave == "forma_pagamento":
                print(f"\033[91mForma de Pagamento\033[0m: {pagamento}")
            else:
                print(f"\033[91m{chave.capitalize()}\033[0m: {valor}")

        input("\nPressione ENTER para continuar...")
        return True
    
    except (KeyboardInterrupt, EOFError):
        print("\n\nVoltando ao menu...")
        input("\nPressione ENTER para continuar...")
        return None


if __name__ == "__main__":
    despesa_registro()