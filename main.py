from database.banco import criar_tabela
import services

def escolha_menu():
    while True:
        services.utils.logo_main()
        print("""===== escolha =====""".upper())
        print("""
[1] - Novo Pagamento
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
                services.utils.encerrar()
                break

            else:
                print("\nOpção inválida!")
                input("\nPressione ENTER para continuar...")

        except EOFError:
            services.utils.encerrar()
            break

def main():
    criar_tabela()
    try:
        services.utils.limpar()
        escolha_menu()

    except KeyboardInterrupt:
        services.utils.encerrar()
    
    except EOFError:
        services.utils.encerrar ()


if __name__ == "__main__":
    main()