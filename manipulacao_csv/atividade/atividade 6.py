import csv


# Carregar treinadores
def carregar_treinadores():
    treinadores = []

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for treinador in leitor:
            treinadores.append(treinador)

    return treinadores


# Carregar Pokémon
def carregar_pokemons():
    pokemons = []

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for pokemon in leitor:
            pokemons.append(pokemon)

    return pokemons


# 1 - Listar treinadores
def listar_treinadores(treinadores):
    print("\n===== TREINADORES =====")

    for treinador in treinadores:
        print(
            f"Nome: {treinador['nome']} - "
            f"Região: {treinador['regiao']} - "
            f"Nível: {treinador['nivel']}"
        )


# 2 - Consultar equipe
def consultar_equipe(treinadores, pokemons):

    nome = input("Digite o nome do treinador: ").strip().lower()

    treinador_encontrado = None

    # Procurar o treinador
    for treinador in treinadores:
        if treinador["nome"].lower() == nome:
            treinador_encontrado = treinador
            break

    if treinador_encontrado is None:
        print("Treinador não encontrado.")
        return

    print("\n===== EQUIPE =====")
    print(f"Treinador: {treinador_encontrado['nome']}")
    print(f"Região: {treinador_encontrado['regiao']}")
    print(f"Nível: {treinador_encontrado['nivel']}")

    print("\nPokémon da equipe:")

    numero = 1

    for pokemon in pokemons:

        if pokemon["treinador"].lower() == nome:

            print(
                f"{numero} - "
                f"{pokemon['nome']} - "
                f"{pokemon['tipo']} - "
                f"{pokemon['nivel']}"
            )

            numero += 1

    if numero == 1:
        print("Nenhum Pokémon encontrado.")


# 3 - Calcular pontuação
def calcular_pontuacao(treinadores, pokemons):

    resultados = []

    for treinador in treinadores:

        nome = treinador["nome"]

        nivel_treinador = int(treinador["nivel"])

        quantidade_pokemons = 0
        soma_niveis = 0

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():

                nivel_pokemon = int(pokemon["nivel"])

                quantidade_pokemons += 1
                soma_niveis += nivel_pokemon

        pontuacao = nivel_treinador + soma_niveis

        resultado = {
            "treinador": nome,
            "regiao": treinador["regiao"],
            "nivel_treinador": nivel_treinador,
            "quantidade_pokemon": quantidade_pokemons,
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao
        }

        resultados.append(resultado)

    return resultados


# 4 - Mostrar classificação
def mostrar_classificacao(treinadores, pokemons):

    resultados = calcular_pontuacao(
        treinadores,
        pokemons
    )

    # Ordenar do maior para o menor
    resultados.sort(
        key=lambda resultado: resultado["pontuacao"],
        reverse=True
    )

    print("\n===== CLASSIFICAÇÃO =====")

    posicao = 1

    for resultado in resultados:

        print(
            f"{posicao}º - "
            f"{resultado['treinador']} - "
            f"{resultado['pontuacao']} pontos"
        )

        posicao += 1


# 5 - Gerar CSV do campeonato
def gerar_csv_campeonato(treinadores, pokemons):

    resultados = calcular_pontuacao(
        treinadores,
        pokemons
    )

    # Ordenar do maior para o menor
    resultados.sort(
        key=lambda resultado: resultado["pontuacao"],
        reverse=True
    )

    nome_arquivo = "resultado_campeonato.csv"

    with open(
        nome_arquivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        campos = [
            "treinador",
            "regiao",
            "nivel_treinador",
            "quantidade_pokemon",
            "soma_niveis",
            "pontuacao"
        ]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for resultado in resultados:
            escritor.writerow(resultado)

    print(f"\nArquivo criado: {nome_arquivo}")
    print(f"Registros gravados: {len(resultados)}")


# Menu principal
def menu():

    treinadores = carregar_treinadores()
    pokemons = carregar_pokemons()

    while True:

        print("\n===== CAMPEONATO POKÉMON =====")
        print("1 - Listar treinadores")
        print("2 - Consultar equipe")
        print("3 - Calcular pontuação")
        print("4 - Mostrar classificação")
        print("5 - Gerar arquivo CSV do campeonato")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_treinadores(treinadores)

        elif opcao == "2":
            consultar_equipe(
                treinadores,
                pokemons
            )

        elif opcao == "3":

            resultados = calcular_pontuacao(
                treinadores,
                pokemons
            )

            print("\n===== PONTUAÇÃO =====")

            for resultado in resultados:

                print(
                    f"Treinador: {resultado['treinador']}"
                )

                print(
                    f"Quantidade de Pokémon: "
                    f"{resultado['quantidade_pokemon']}"
                )

                print(
                    f"Soma dos níveis: "
                    f"{resultado['soma_niveis']}"
                )

                print(
                    f"Pontuação: "
                    f"{resultado['pontuacao']}"
                )

                print()

        elif opcao == "4":
            mostrar_classificacao(
                treinadores,
                pokemons
            )

        elif opcao == "5":
            gerar_csv_campeonato(
                treinadores,
                pokemons
            )

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()