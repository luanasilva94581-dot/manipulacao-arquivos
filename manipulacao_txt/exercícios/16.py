def buscar_produto():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    busca = input("Digite o produto: ")

    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            print("Produto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")

            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado!")


buscar_produto()