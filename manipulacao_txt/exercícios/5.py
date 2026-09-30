def contar_caracteres():
    with open("texto.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Python")

    quantidade = 0

    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        quantidade = len(texto)

    print(f"Quantidade de caracteres: {quantidade}")


contar_caracteres()