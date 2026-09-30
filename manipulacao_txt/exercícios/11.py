def listar_aprovados():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")
        arquivo.write("Eduardo;4.5\n")
        arquivo.write("Fernanda;6.8\n")
        arquivo.write("Gabriel;5.9\n")

    print("Alunos aprovados:")

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            if nota >= 6.0:
                print(f"{nome} - {nota}")


listar_aprovados()