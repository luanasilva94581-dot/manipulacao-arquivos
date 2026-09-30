def carregar_nomes():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            nomes.append(nome)

    print(nomes)


carregar_nomes()