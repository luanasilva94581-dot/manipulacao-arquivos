def ler_arquivo():
    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá, Mundo!")
        arquivo.write("Estou aprendendo Python")
        arquivo.write("Estou estudando manipulação de arquivos.")

    with open ("mensagem.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteudo do arquivo é: {conteudo}")
ler_arquivo()