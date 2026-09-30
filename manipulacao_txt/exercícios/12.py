def classificar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            if nota >= 6:
                situacao = "Aprovado"
            elif nota >= 4:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print(f"{nome} - {nota} - {situacao}")


classificar_alunos()