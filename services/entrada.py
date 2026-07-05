import database
import services
from datetime import datetime

def entrada_registro():
    try:
        services.utils.logo_register()
        print("\n=== Nova Entrada===".upper())
        valor = services.utils.pedir_valor("\n\033[36mValor\033[0m (R$): ")
        print("---------------")

        print("""\nForma de \033[36mRecebimento\033[0m:
[1] PIX
[2] Dinheiro
[3] Cartão
[4] Depósito
[0] Não informar""")

        formas = {
            "1": "PIX",
            "2": "Dinheiro",
            "3": "Cartão",
            "4": "Depósito",
            "0": "Não informado"
        }

        while True:
            recebimento = input("\nEscolha: ").strip()
        
            if recebimento in formas:
                recebimento = formas[recebimento]
                print("---------------")

                if recebimento in ("PIX", "Cartão", "Depósito"):
                    banco = services.utils.pedir_banco()
                    print("---------------")

                else:
                    banco = "Não se aplica"
                break

            print("Digite apenas o número correpondente!")
        
        origem = input("\n\033[36mOrigem\033[0m: ").strip()

        if origem == "":
            origem = "Não informado"
        print("---------------")

        data = services.utils.pedir_data ("\n\033[36mData\033[0m (DD/MM/AAAA): ")
        print("---------------")
        hora = services.utils.pedir_hora("\n\033[36mHora\033[0m (HH:MM): ")
        print("---------------")
        

        remetente = input("\n\033[36mRemetente\033[0m: ").strip()
        if remetente == "":
            remetente = "Não informado"
        
        print("---------------")
        
        registro = {
            "tipo":"Entrada",
            "valor": valor,
            "forma_pagamento": recebimento,
            "banco": banco,
            "local": origem,
            "data": data,
            "hora": hora,
            "cnpj": remetente
        }

        database.banco.salvar_registro(registro)
        
        print("""
============================
      REGISTRO CRIADO
============================
""")
        
        for chave, valor in registro.items():

            if chave == "valor":
                print(f"\033[92mValor\033[0m: R$ {valor:.2f}")
            elif chave == "forma_pagamento":
                print(f"\033[92mForma de Pagamento\033[0m: {recebimento}")            
            else:
                print(f"\033[92m{chave.capitalize()}\033[0m: {valor}")

        input("\nPressione ENTER para continuar...")
        return True
    
    except (KeyboardInterrupt, EOFError):
        print("\n\nVoltando ao menu...")
        input("\nPressione ENTER para continuar...")
        return None

if __name__ == "__main__":
    entrada_registro()