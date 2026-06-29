from database.banco import criar_tabela
import services
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
        logo()
        print("""===== escolha =====""".upper())
        print("""
[1] - Novo pagamento
[2] - Listar Pendentes
[3] - Exportar Excel
[0] - Sair
    """)
            
        opcao = input("> ").strip()
        try:
            if opcao == "1":
                services.financeiro.novo_registro()

            elif opcao == "2":
                services.financeiro.listar_pendentes()

            elif opcao == "3":
                services.excel.exportar_excel()

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
    criar_tabela()
    try:
        limpar()
        escolha_menu()

    except KeyboardInterrupt:
        encerrar()
    
    except EOFError:
        encerrar ()


if __name__ == "__main__":
    main()