def contar_palavras():
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palavras = texto.split()

    print(f"Quantidade de palavras: {len(palavras)}")


contar_palavras()

