def gerar_relatorio():
    # Criando o arquivo vendas.txt
    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\n")
        arquivo.write("Bruno;Mouse;80.00\n")
        arquivo.write("Carlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\n")
        arquivo.write("Daniela;Notebook;3500.00\n")
        arquivo.write("Bruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\n")
        arquivo.write("Ana;Teclado;150.00\n")
        arquivo.write("Daniela;Monitor;900.00\n")

    vendas = []

    # Lendo o arquivo e criando os dicionários
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    # Exibindo todas as vendas
    print("VENDAS:")

    for venda in vendas:
        print(
            f"{venda['vendedor']} - "
            f"{venda['produto']} - "
            f"R$ {venda['valor']:.2f}"
        )

    # Calculando o valor total das vendas
    total_vendas = 0

    for venda in vendas:
        total_vendas += venda["valor"]

    print(f"\nTOTAL DE VENDAS: R$ {total_vendas:.2f}")

    # Contando quantas vendas cada vendedor realizou
    quantidade_vendas = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print("\nQuantidade de vendas:")

    for vendedor, quantidade in quantidade_vendas.items():
        print(f"{vendedor}: {quantidade}")

    # Desafio: vendedor com maior valor total em vendas
    total_por_vendedor = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        if vendedor in total_por_vendedor:
            total_por_vendedor[vendedor] += valor
        else:
            total_por_vendedor[vendedor] = valor

    maior_vendedor = ""
    maior_valor = 0

    for vendedor, valor in total_por_vendedor.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_vendedor = vendedor

    print(
        f"\nMaior valor total em vendas: "
        f"{maior_vendedor} - R$ {maior_valor:.2f}"
    )


gerar_relatorio()