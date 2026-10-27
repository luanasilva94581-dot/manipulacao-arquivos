
import csv
from pathlib import Path

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

treinadores = []
pokemons = []

# Ler os treinadores e os Pokémon
if arquivo_treinadores is None or arquivo_pokemons is None:
    print("Erro: não foi possível encontrar os arquivos CSV.")
    print("Coloque os arquivos na pasta do projeto ou em uma pasta acima.")

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
    def relatorio_treinador():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        print("\nTreinador:", treinador_encontrado["nome"])
        print("Região:", treinador_encontrado["regiao"])
        print("Nível do treinador:", treinador_encontrado["nivel"])
        print("\nPokémon:")

        equipe = []

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                equipe.append(pokemon)

        if not equipe:
            print("Esse treinador não possui Pokémon cadastrados.")
            return

        for pokemon in equipe:
            print(
                "-",
                pokemon["nome"],
                "-",
                pokemon["tipo"],
                "- Nível",
                pokemon["nivel"]
            )

    # Opção 2
    def media_pokemons_treinador():
        nome_busca = input("Digite o nome do treinador: ").strip()
        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        soma = 0
        quantidade = 0

        for pokemon in pokemons:
            if pokemon["treinador"].strip().lower() == treinador_encontrado["nome"].strip().lower():
                soma += int(pokemon["nivel"])
                quantidade += 1

        if quantidade == 0:
            print("Esse treinador não possui Pokémon cadastrados.")
        else:
            media = soma / quantidade
            print("Treinador:", treinador_encontrado["nome"])
            print("Média de nível dos Pokémon:", round(media, 2))

    # Opção 3
    def media_pokemons_tipo():
        tipo_busca = input("Digite o tipo do Pokémon: ").strip()

        soma = 0
        quantidade = 0

        for pokemon in pokemons:
            if pokemon["tipo"].strip().lower() == tipo_busca.lower():
                soma += int(pokemon["nivel"])
                quantidade += 1

        if quantidade == 0:
            print("Nenhum Pokémon encontrado desse tipo.")
        else:
            media = soma / quantidade
            print("Tipo:", tipo_busca)
            print("Quantidade de Pokémon:", quantidade)
            print("Média de nível:", round(media, 2))

    # Opção 4
    def quantidade_por_treinador():
        quantidades = {}

        for treinador in treinadores:
            quantidades[treinador["nome"]] = 0

        for pokemon in pokemons:
            nome_treinador = pokemon["treinador"].strip()

            for treinador in treinadores:
                if treinador["nome"].strip().lower() == nome_treinador.lower():
                    nome_correto = treinador["nome"]
                    quantidades[nome_correto] += 1
                    break

        ordenados = sorted(
            quantidades.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n--- QUANTIDADE DE POKÉMON POR TREINADOR ---")

        for nome, quantidade in ordenados:
            print(nome, ":", quantidade)

    # Opção 5
    def quantidade_por_tipo():
        quantidades = {}

        for pokemon in pokemons:
            tipo = pokemon["tipo"].strip()

            if tipo in quantidades:
                quantidades[tipo] += 1
            else:
                quantidades[tipo] = 1

        ordenados = sorted(
            quantidades.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n--- QUANTIDADE DE POKÉMON POR TIPO ---")

        for tipo, quantidade in ordenados:
            print(tipo, ":", quantidade)

    # Opção 6
    def treinadores_acima_nivel():
        valor = int(input("Digite o nível mínimo: "))
        encontrados = []

        for treinador in treinadores:
            if int(treinador["nivel"]) > valor:
                encontrados.append(treinador)

        if not encontrados:
            print("Nenhum treinador possui nível acima desse valor.")
            return

        encontrados.sort(
            key=lambda treinador: int(treinador["nivel"]),
            reverse=True
        )

        print("\n--- TREINADORES ACIMA DO NÍVEL", valor, "---")

        for treinador in encontrados:
            print("Nome:", treinador["nome"])
            print("Região:", treinador["regiao"])
            print("Nível:", treinador["nivel"])
            print()

    # Menu principal
    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório de um treinador")
        print("2 - Média de nível dos Pokémon de um treinador")
        print("3 - Média de nível dos Pokémon por tipo")
        print("4 - Quantidade de Pokémon por treinador")
        print("5 - Quantidade de Pokémon por tipo")
        print("6 - Treinadores com nível acima de um valor")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            relatorio_treinador()

        elif opcao == "2":
            media_pokemons_treinador()

        elif opcao == "3":
            media_pokemons_tipo()

        elif opcao == "4":
            quantidade_por_treinador()

        elif opcao == "5":
            quantidade_por_tipo()

        elif opcao == "6":
            treinadores_acima_nivel()

        elif opcao == "7":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
