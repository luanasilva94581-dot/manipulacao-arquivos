
import csv
from pathlib import Path

treinadores = []
pokemons = []

# Localizar os arquivos CSV
pasta_atual = Path(__file__).resolve().parent


def localizar_arquivo(nome):
    for pasta in [pasta_atual, *pasta_atual.parents]:
        caminho = pasta / nome

        if caminho.exists():
            return caminho

    return None


arquivo_treinadores = localizar_arquivo("treinadores.csv")
arquivo_pokemons = localizar_arquivo("pokemons.csv")


# Ler os arquivos
if arquivo_treinadores is None or arquivo_pokemons is None:
    print("Erro: não foi possível encontrar os arquivos CSV.")
    print("Verifique se os arquivos estão na pasta do projeto.")

else:
    with open(arquivo_treinadores, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for treinador in leitor:
            treinadores.append(treinador)

    with open(arquivo_pokemons, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for pokemon in leitor:
            pokemons.append(pokemon)

    # Opção 1
    def listar_pokemons():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        equipe = []

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                equipe.append(pokemon)

        if not equipe:
            print("Esse treinador não possui Pokémon cadastrados.")
            return

        print("\nPokémon de", treinador_encontrado["nome"], ":")

        for pokemon in equipe:
            print("Nome:", pokemon["nome"])
            print("Tipo:", pokemon["tipo"])
            print("Nível:", pokemon["nivel"])
            print()

    # Opção 2
    def contar_pokemons():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        quantidade = 0

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                quantidade += 1

        print("Treinador:", treinador_encontrado["nome"])
        print("Quantidade de Pokémon:", quantidade)

    # Opção 3
    def mostrar_maior_nivel():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        equipe = []

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                equipe.append(pokemon)

        if not equipe:
            print("Esse treinador não possui Pokémon cadastrados.")
            return

        maior = equipe[0]

        for pokemon in equipe:
            if int(pokemon["nivel"]) > int(maior["nivel"]):
                maior = pokemon

        print("\nPokémon de maior nível:")
        print("Nome:", maior["nome"])
        print("Tipo:", maior["tipo"])
        print("Nível:", maior["nivel"])

    # Opção 4
    def mostrar_menor_nivel():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        equipe = []

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                equipe.append(pokemon)

        if not equipe:
            print("Esse treinador não possui Pokémon cadastrados.")
            return

        menor = equipe[0]

        for pokemon in equipe:
            if int(pokemon["nivel"]) < int(menor["nivel"]):
                menor = pokemon

        print("\nPokémon de menor nível:")
        print("Nome:", menor["nome"])
        print("Tipo:", menor["tipo"])
        print("Nível:", menor["nivel"])

    # Opção 5
    def listar_por_tipo():
        tipo_busca = input("Digite o tipo do Pokémon: ").strip()
        encontrados = []

        for pokemon in pokemons:
            if pokemon["tipo"].strip().lower() == tipo_busca.lower():
                encontrados.append(pokemon)

        if not encontrados:
            print("Nenhum Pokémon encontrado desse tipo.")
            return

        print("\nPokémon do tipo", tipo_busca, ":")

        for pokemon in encontrados:
            print("Nome:", pokemon["nome"])
            print("Tipo:", pokemon["tipo"])
            print("Nível:", pokemon["nivel"])
            print("Treinador:", pokemon["treinador"])
            print()

    # Menu principal
    while True:
        print("\n===== POKÉMON DOS TREINADORES =====")
        print("1 - Listar Pokémon de um treinador")
        print("2 - Contar Pokémon de um treinador")
        print("3 - Mostrar Pokémon de maior nível")
        print("4 - Mostrar Pokémon de menor nível")
        print("5 - Listar Pokémon de determinado tipo")
        print("6 - Voltar ao menu")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_pokemons()

        elif opcao == "2":
            contar_pokemons()

        elif opcao == "3":
            mostrar_maior_nivel()

        elif opcao == "4":
            mostrar_menor_nivel()

        elif opcao == "5":
            listar_por_tipo()

        elif opcao == "6":
            print("Voltando...")
            break

        else:
            print("Opção inválida. Tente novamente.")
