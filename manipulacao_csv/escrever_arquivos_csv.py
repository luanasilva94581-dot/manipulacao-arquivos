import  csv
from idlelib.iomenu import encoding


def criar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "curso"])

        escritor.writerow(["Lua", 17, "Dev"])
        escritor.writerow(["duda", 23, "Nutri"])
        escritor.writerow(["deh", 24, "Medicina"])

#criar_csv()


def salvar_alunos():
    alunos = [
        ["Lua", 17, "Dev"],
        ["Duda", 23, "Nutri"],
        ["Deh", 24, "Medicina"],
        ["Feh", 25, "Dono da zoe piscina"],
        ["Ana", 17, "Atleta"]
    ]


    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)


        for linha in leitor:
            print(linha[0])

#ler_csv()

def exivir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno["Curso"])

#exivir_alunos()



def cadastrar_alunos():
    with open("novos_alunos.csv", "a+", encoding="utf-8") as arquivo:
        # Move o curso para o final do arquivo
        arquivo.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, curso])

        # Move o curso para o início do arquivo
        arquivo.seek(0)
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(linha["Curso"])

# cadastrar_alunos()

def deletar_aluno():

    with open("novos_alunos.csv", "r", newline="",encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        cabecalho = ["Nome", "Idade", "Curso"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        aluno_apagar = input("Digite o nome do aluno que deseja apagar: ")

        for aluno in alunos:
            if aluno["nome"] != aluno_apagar:
                escritor.writerow(aluno)

deletar_aluno()














