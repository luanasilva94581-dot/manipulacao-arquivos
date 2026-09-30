def criar_arquivo():
    frase = input("Digite uma frase: ")

    with open("frase.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)


criar_arquivo()