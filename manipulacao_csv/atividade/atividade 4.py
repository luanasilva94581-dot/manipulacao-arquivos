
import csv
from pathlib import Path

# Localizar os arquivos
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

# Ler os treinadores
if arquivo_treinadores is not None:
    with open(arquivo_treinadores, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for treinador in leitor:
            treinadores.append(treinador)

# Ler os Pokémon
if arquivo_pokemons is not None:
    with open(arquivo_pokemons, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for pokemon in leitor:
            pokemons.append(pokemon)


def listar_treinadores():
    print("\n--- TREINADORES CADASTRADOS ---")

    for treinador in treinadores:
        print("-", treinador["nome"])


def gerar_csv_treinador():
    nome_busca = input("Digite o treinador: ").strip()
    treinador_encontrado = None

    for treinador in treinadores:
        if treinador["nome"].strip().lower() == nome_busca.lower():
            treinador_encontrado = treinador
            break

    if treinador_encontrado is None:
        print("Treinador não encontrado.")
        return

    nome_correto = treinador_encontrado["nome"].strip()

    equipe = []

    for pokemon in pokemons:
        if pokemon["treinador"].strip().lower() == nome_correto.lower():
            equipe.append({
                "nome": pokemon["nome"],
                "tipo": pokemon["tipo"],
                "nivel": pokemon["nivel"],
                "treinador": nome_correto
            })

    # Criar o nome do arquivo
    nome_arquivo = nome_correto.lower().replace(" ", "_")
    caminho_saida = pasta_atual / f"pokemons_{nome_arquivo}.csv"

    colunas = ["nome", "tipo", "nivel", "treinador"]

    with open(caminho_saida, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(equipe)

    print("\nArquivo criado:", caminho_saida.name)
    print("Quantidade de Pokémon gravados:", len(equipe))


def gerar_csv_todos():
    # Ordenar os Pokémon pelo nível, do menor para o maior
    pokemons_ordenados = sorted(
        pokemons,
        key=lambda pokemon: int(pokemon["nivel"])
    )

    colunas = ["nome", "tipo", "nivel", "treinador"]

    caminho_saida = pasta_atual / "todos_pokemons_ordenados.csv"

    with open(caminho_saida, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(pokemons_ordenados)

    print("\nArquivo criado: todos_pokemons_ordenados.csv")
    print("Quantidade de Pokémon gravados:", len(pokemons_ordenados))


# Verificar se os arquivos existem
if arquivo_treinadores is None or arquivo_pokemons is None:
    print("Erro: não foi possível encontrar os arquivos CSV.")
    print("Verifique se treinadores.csv e pokemons.csv estão no projeto.")

else:
    while True:
        print("\n===== GERADOR DE ARQUIVOS =====")
        print("1 - Listar treinadores")
        print("2 - Gerar CSV de um treinador")
        print("3 - Gerar CSV de todos os treinadores")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_treinadores()

        elif opcao == "2":
            gerar_csv_treinador()

        elif opcao == "3":
            gerar_csv_todos()

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
