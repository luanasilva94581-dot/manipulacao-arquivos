def carregar_alunos():
    alunos = []

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_aluno, nome, idade, curso = linha.strip().split(";")

            aluno = {
                "id": int(id_aluno),
                "nome": nome,
                "idade": int(idade),
                "curso": curso
            }

            alunos.append(aluno)

    return alunos


def salvar_alunos(alunos):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['id']};"
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['curso']}\n"
            )


def listar_alunos(alunos):
    print("\n===== LISTA DE ALUNOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(
                f"{aluno['id']} - "
                f"{aluno['nome']} - "
                f"{aluno['idade']} anos"
            )


def buscar_aluno(alunos):
    id_busca = int(input("Digite o ID: "))

    aluno_encontrado = None

    for aluno in alunos:
        if aluno["id"] == id_busca:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
        print("\nAluno encontrado:")
        print(aluno_encontrado["nome"])
        print(f"{aluno_encontrado['idade']} anos")
        print(aluno_encontrado["curso"])
    else:
        print("Aluno não encontrado!")


def cadastrar_aluno(alunos):
    print("\n===== CADASTRAR ALUNO =====")

    if len(alunos) == 0:
        novo_id = 1
    else:
        maior_id = 0

        for aluno in alunos:
            if aluno["id"] > maior_id:
                maior_id = aluno["id"]

        novo_id = maior_id + 1

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    salvar_alunos(alunos)

    print("\nAluno cadastrado com sucesso!")
    print(f"ID do aluno: {novo_id}")


def remover_aluno(alunos):
    id_remover = int(input("Digite o ID do aluno que deseja remover: "))

    aluno_encontrado = None

    for aluno in alunos:
        if aluno["id"] == id_remover:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
        alunos.remove(aluno_encontrado)
        salvar_alunos(alunos)

        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado!")


def alterar_aluno(alunos):
    id_alterar = int(input("Digite o ID do aluno que deseja alterar: "))

    aluno_encontrado = None

    for aluno in alunos:
        if aluno["id"] == id_alterar:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
        print("\nAluno encontrado!")

        novo_nome = input("Digite o novo nome: ")
        nova_idade = int(input("Digite a nova idade: "))
        novo_curso = input("Digite o novo curso: ")

        aluno_encontrado["nome"] = novo_nome
        aluno_encontrado["idade"] = nova_idade
        aluno_encontrado["curso"] = novo_curso

        salvar_alunos(alunos)

        print("Aluno alterado com sucesso!")
    else:
        print("Aluno não encontrado!")


def sistema_alunos():

    # Criando o arquivo com os alunos iniciais
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(
            "1;Ana Silva;17;Desenvolvimento de Sistemas\n"
        )
        arquivo.write(
            "2;Bruno Souza;18;Desenvolvimento de Sistemas\n"
        )
        arquivo.write(
            "3;Carlos Oliveira;17;Desenvolvimento de Sistemas\n"
        )
        arquivo.write(
            "4;Daniela Santos;18;Desenvolvimento de Sistemas\n"
        )
        arquivo.write(
            "5;Eduardo Lima;17;Desenvolvimento de Sistemas\n"
        )

    # Carregando os alunos do arquivo
    alunos = carregar_alunos()

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_alunos(alunos)

        elif opcao == "2":
            buscar_aluno(alunos)

        elif opcao == "3":
            cadastrar_aluno(alunos)

        elif opcao == "4":
            remover_aluno(alunos)

        elif opcao == "5":
            alterar_aluno(alunos)

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


sistema_alunos()