from services.financeiro import novo_registro
from services.excel import exportar_excel
import os

VERSAO = "0.1"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def encerrar():
    print("\n\nEncerrando...")
    input("\nPressione ENTER para continuar...")
    limpar()

def logo():
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
        
def escolha_menu():
    while True:
        limpar()
        logo()
        print("""===== escolha =====""".upper())
        print("""
[1] - Novo pagamento
[2] - Exportar Excel
[0] - Sair
    """)
            
        opcao = input("> ").strip()
        try:
            if opcao == "1":
                novo_registro()

            elif opcao == "2":
                exportar_excel()

            elif opcao == "0":
                encerrar()
                break

            else:
                print("\nOpção inválida!")
                input("\nPressione ENTER para continuar...")

        except EOFError:
            encerrar()
            break

def main():
    try:
        limpar()
        escolha_menu()

    except KeyboardInterrupt:
        encerrar()
    
    except EOFError:
        encerrar ()


if __name__ == "__main__":
    main()