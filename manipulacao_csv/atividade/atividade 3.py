import csv


# Carrega os treinadores do arquivo CSV
def carregar_treinadores():
    treinadores = []

    try:
        with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for treinador in leitor:
                treinadores.append(treinador)

    except FileNotFoundError:
        print("Arquivo treinadores.csv não encontrado.")

    return treinadores


# Carrega os Pokémon do arquivo CSV
def carregar_pokemons():
    pokemons = []

    try:
        with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for pokemon in leitor:
                pokemons.append(pokemon)

    except FileNotFoundError:
        print("Arquivo pokemons.csv não encontrado.")

    return pokemons


# 1 - Relatório de um treinador
def relatorio_treinador(treinadores, pokemons):
    nome = input("Digite o nome do treinador: ").strip().lower()

    treinador_encontrado = None

    for treinador in treinadores:
        if treinador["nome"].lower() == nome:
            treinador_encontrado = treinador
            break

    if treinador_encontrado is None:
        print("Treinador não encontrado.")
        return

    print("\n===== RELATÓRIO =====")
    print(f"Treinador: {treinador_encontrado['nome']}")
    print(f"Região: {treinador_encontrado['regiao']}")
    print(f"Nível do treinador: {treinador_encontrado['nivel']}")

    print("\nPokémon:")

    for pokemon in pokemons:
        if pokemon["treinador"].lower() == nome:
            print(
                f"- {pokemon['nome']} - "
                f"{pokemon['tipo']} - "
                f"Nível {pokemon['nivel']}"
            )


# 2 - Média de nível dos Pokémon de um treinador
def media_pokemon_treinador(pokemons):
    nome = input("Digite o nome do treinador: ").strip().lower()

    soma = 0
    quantidade = 0

    for pokemon in pokemons:
        if pokemon["treinador"].lower() == nome:
            nivel = int(pokemon["nivel"])

            soma += nivel
            quantidade += 1

    if quantidade == 0:
        print("Nenhum Pokémon encontrado.")
    else:
        media = soma / quantidade
        print(f"Média de nível dos Pokémon: {media:.2f}")


# 3 - Média de nível dos Pokémon por tipo
def media_pokemon_tipo(pokemons):
    tipo = input("Digite o tipo do Pokémon: ").strip().lower()

    soma = 0
    quantidade = 0

    for pokemon in pokemons:
        if pokemon["tipo"].lower() == tipo:
            nivel = int(pokemon["nivel"])

            soma += nivel
            quantidade += 1

    if quantidade == 0:
        print("Nenhum Pokémon encontrado desse tipo.")
    else:
        media = soma / quantidade
        print(f"Média de nível do tipo {tipo}: {media:.2f}")


# 4 - Quantidade de Pokémon por treinador
def quantidade_por_treinador(pokemons):
    quantidade = {}

    for pokemon in pokemons:
        treinador = pokemon["treinador"]

        if treinador not in quantidade:
            quantidade[treinador] = 0

        quantidade[treinador] += 1

    resultado = sorted(
        quantidade.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n===== POKÉMON POR TREINADOR =====")

    for treinador, total in resultado:
        print(f"{treinador}: {total}")


# 5 - Quantidade de Pokémon por tipo
def quantidade_por_tipo(pokemons):
    quantidade = {}

    for pokemon in pokemons:
        tipo = pokemon["tipo"]

        if tipo not in quantidade:
            quantidade[tipo] = 0

        quantidade[tipo] += 1

    resultado = sorted(
        quantidade.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n===== POKÉMON POR TIPO =====")

    for tipo, total in resultado:
        print(f"{tipo}: {total}")


# 6 - Treinadores com nível acima de um valor
def treinadores_acima_nivel(treinadores):
    nivel = int(input("Digite o nível mínimo: "))

    encontrados = []

    for treinador in treinadores:
        nivel_treinador = int(treinador["nivel"])

        if nivel_treinador > nivel:
            encontrados.append(treinador)

    if encontrados:
        print("\n===== TREINADORES =====")

        for treinador in encontrados:
            print(
                f"{treinador['nome']} - "
                f"Nível {treinador['nivel']} - "
                f"Região: {treinador['regiao']}"
            )
    else:
        print("Nenhum treinador encontrado.")


# Menu principal
def menu():
    treinadores = carregar_treinadores()
    pokemons = carregar_pokemons()

    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório de um treinador")
        print("2 - Média de nível dos Pokémon de um treinador")
        print("3 - Média de nível dos Pokémon por tipo")
        print("4 - Quantidade de Pokémon por treinador")
        print("5 - Quantidade de Pokémon por tipo")
        print("6 - Treinadores com nível acima de um valor")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_treinador(treinadores, pokemons)

        elif opcao == "2":
            media_pokemon_treinador(pokemons)

        elif opcao == "3":
            media_pokemon_tipo(pokemons)

        elif opcao == "4":
            quantidade_por_treinador(pokemons)

        elif opcao == "5":
            quantidade_por_tipo(pokemons)

        elif opcao == "6":
            treinadores_acima_nivel(treinadores)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()