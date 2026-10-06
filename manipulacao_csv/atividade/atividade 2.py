import csv


# Carregar os treinadores
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


# Carregar os Pokémon
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


# Procurar os Pokémon de um treinador
def buscar_pokemons_treinador(treinadores, pokemons):
    nome = input("Digite o nome do treinador: ").strip().lower()

    treinador_encontrado = None

    # Procurar o treinador
    for treinador in treinadores:
        if treinador["nome"].lower() == nome:
            treinador_encontrado = treinador
            break

    if treinador_encontrado is None:
        print("Treinador não encontrado.")
        return []

    # Lista para guardar os Pokémon encontrados
    pokemons_treinador = []

    for pokemon in pokemons:
        if pokemon["treinador"].lower() == nome:
            pokemons_treinador.append(pokemon)

    return pokemons_treinador


# 1 - Listar Pokémon de um treinador
def listar_pokemons(treinadores, pokemons):
    pokemons_treinador = buscar_pokemons_treinador(
        treinadores,
        pokemons
    )

    if pokemons_treinador:
        print("\n===== POKÉMON DO TREINADOR =====")

        for pokemon in pokemons_treinador:
            print(
                f"{pokemon['nome']} - "
                f"{pokemon['tipo']} - "
                f"Nível {pokemon['nivel']}"
            )
    else:
        print("Nenhum Pokémon encontrado.")


# 2 - Contar Pokémon de um treinador
def contar_pokemons(treinadores, pokemons):
    pokemons_treinador = buscar_pokemons_treinador(
        treinadores,
        pokemons
    )

    if pokemons_treinador:
        quantidade = len(pokemons_treinador)

        print(f"Quantidade de Pokémon: {quantidade}")
    else:
        print("Nenhum Pokémon encontrado.")


# 3 - Mostrar Pokémon de maior nível
def maior_nivel(treinadores, pokemons):
    pokemons_treinador = buscar_pokemons_treinador(
        treinadores,
        pokemons
    )

    if pokemons_treinador:
        maior = max(
            pokemons_treinador,
            key=lambda pokemon: int(pokemon["nivel"])
        )

        print(
            f"Maior nível: {maior['nome']} "
            f"- Nível {maior['nivel']}"
        )
    else:
        print("Nenhum Pokémon encontrado.")


# 4 - Mostrar Pokémon de menor nível
def menor_nivel(treinadores, pokemons):
    pokemons_treinador = buscar_pokemons_treinador(
        treinadores,
        pokemons
    )

    if pokemons_treinador:
        menor = min(
            pokemons_treinador,
            key=lambda pokemon: int(pokemon["nivel"])
        )

        print(
            f"Menor nível: {menor['nome']} "
            f"- Nível {menor['nivel']}"
        )
    else:
        print("Nenhum Pokémon encontrado.")


# 5 - Listar Pokémon de determinado tipo
def listar_por_tipo(pokemons):
    tipo = input("Digite o tipo do Pokémon: ").strip().lower()

    encontrados = []

    for pokemon in pokemons:
        if pokemon["tipo"].lower() == tipo:
            encontrados.append(pokemon)

    if encontrados:
        print("\n===== POKÉMON DO TIPO =====")

        for pokemon in encontrados:
            print(
                f"{pokemon['nome']} - "
                f"Treinador: {pokemon['treinador']} - "
                f"Nível {pokemon['nivel']}"
            )
    else:
        print("Nenhum Pokémon desse tipo encontrado.")


# Menu
def menu():
    treinadores = carregar_treinadores()
    pokemons = carregar_pokemons()

    while True:
        print("\n===== POKÉMON DOS TREINADORES =====")
        print("1 - Listar Pokémon de um treinador")
        print("2 - Contar Pokémon de um treinador")
        print("3 - Mostrar Pokémon de maior nível")
        print("4 - Mostrar Pokémon de menor nível")
        print("5 - Listar Pokémon de determinado tipo")
        print("6 - Voltar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_pokemons(treinadores, pokemons)

        elif opcao == "2":
            contar_pokemons(treinadores, pokemons)

        elif opcao == "3":
            maior_nivel(treinadores, pokemons)

        elif opcao == "4":
            menor_nivel(treinadores, pokemons)

        elif opcao == "5":
            listar_por_tipo(pokemons)

        elif opcao == "6":
            print("Voltando ao menu...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()