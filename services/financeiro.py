def novo_registro():

    print("\n=== NOVO PAGAMENTO ===")

    local = input("Local: ")
    data = input("Data: ")
    hora = input("Hora: ")
    valor = input("Valor: ")
    pagamento = input("Forma de pagamento: ")
    cnpj = input("CNPJ (opcional): ")

    print("\nRegistro criado!")
    
    print(f"""
Local: {local}
Data: {data}
Hora: {hora}
Valor: {valor}
Pagamento: {pagamento}
CNPJ: {cnpj}
""")