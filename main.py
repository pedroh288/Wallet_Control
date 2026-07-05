import database
import services
        
def escolha_menu():
    while True:
        services.utils.logo_main()
        print("""===== escolha =====""".upper())
        print("""
[1] - Novo Pagamento
[2] - Nova Entrada
[3] - Listar Pendentes
[4] - Exportar Excel
[0] - Sair
    """)
            
        opcao = input("> ").strip()
        try:
            if opcao == "1":
                services.despesa.despesa_registro()

            elif opcao == "2":
                services.entrada.entrada_registro()

            elif opcao == "3":
                services.utils.listar_pendentes()

            elif opcao == "4":
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
    database.banco.criar_tabela()
    try:
        services.utils.limpar()
        escolha_menu()

    except KeyboardInterrupt:
        services.utils.encerrar()
    
    except EOFError:
        services.utils.encerrar ()


if __name__ == "__main__":
    main()
