
import csv
from pathlib import Path


def localizar_arquivo(nome):
    pasta = Path(__file__).resolve().parent

    for local in [pasta, *pasta.parents]:
        arquivo = local / nome

        if arquivo.exists():
            return arquivo

    return None


def carregar_csv(nome):
    arquivo = localizar_arquivo(nome)

    if arquivo is None:
        print(f"Erro: arquivo {nome} não encontrado!")
        return []

    with open(arquivo, "r", encoding="utf-8-sig", newline="") as f:
        leitor = csv.DictReader(f)
        return list(leitor)


def listar_treinadores(treinadores):
    print("\n===== TREINADORES CADASTRADOS =====")

    for treinador in treinadores:
        print(f"\nNome: {treinador['nome']}")
        print(f"Região: {treinador['regiao']}")
        print(f"Nível: {treinador['nivel']}")


def consultar_equipe(treinadores, pokemons):
    nome = input("Digite o nome do treinador: ").strip().lower()

    treinador_encontrado = None

    for treinador in treinadores:
        if treinador["nome"].strip().lower() == nome:
            treinador_encontrado = treinador
            break

    if treinador_encontrado is None:
        print("Treinador não encontrado!")
        return

    equipe = []

    for pokemon in pokemons:
        if pokemon["treinador"].strip().lower() == nome:
            equipe.append(pokemon)

    print("\n===== EQUIPE DO TREINADOR =====")
    print(f"Treinador: {treinador_encontrado['nome']}")
    print(f"Região: {treinador_encontrado['regiao']}")
    print(f"Nível: {treinador_encontrado['nivel']}")

    print("\nPokémon da equipe:")

    if len(equipe) == 0:
        print("Nenhum Pokémon cadastrado para esse treinador.")
        return

    for i, pokemon in enumerate(equipe, start=1):
        print(
            f"{i} - {pokemon['nome']} - "
            f"{pokemon['tipo']} - {pokemon['nivel']}"
        )


def calcular_pontuacoes(treinadores, pokemons):
    resultados = []

    for treinador in treinadores:
        equipe = []

        for pokemon in pokemons:
            if (
                pokemon["treinador"].strip().lower()
                == treinador["nome"].strip().lower()
            ):
                equipe.append(pokemon)

        soma_niveis = 0

        for pokemon in equipe:
            soma_niveis += int(pokemon["nivel"])

        nivel_treinador = int(treinador["nivel"])
        pontuacao = nivel_treinador + soma_niveis

        resultado = {
            "treinador": treinador["nome"],
            "regiao": treinador["regiao"],
            "nivel_treinador": nivel_treinador,
            "quantidade_pokemons": len(equipe),
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao
        }

        resultados.append(resultado)

    return resultados


def mostrar_pontuacoes(resultados):
    print("\n===== PONTUAÇÃO DOS TREINADORES =====")

    for resultado in resultados:
        print(f"\nTreinador: {resultado['treinador']}")
        print(f"Quantidade de Pokémon: {resultado['quantidade_pokemons']}")
        print(f"Soma dos níveis: {resultado['soma_niveis']}")
        print(f"Pontuação: {resultado['pontuacao']}")


def mostrar_classificacao(resultados):
    classificacao = sorted(
        resultados,
        key=lambda resultado: resultado["pontuacao"],
        reverse=True
    )

    print("\n===== CLASSIFICAÇÃO DO CAMPEONATO =====")

    for posicao, resultado in enumerate(classificacao, start=1):
        print(
            f"{posicao}º lugar - {resultado['treinador']} "
            f"({resultado['regiao']}) - "
            f"Pontuação: {resultado['pontuacao']}"
        )


def gerar_csv(resultados):
    arquivo = localizar_arquivo("treinadores.csv")

    if arquivo is None:
        print("Não foi possível localizar a pasta dos arquivos CSV.")
        return

    caminho_saida = arquivo.parent / "resultado_campeonato.csv"

    campos = [
        "treinador",
        "regiao",
        "nivel_treinador",
        "quantidade_pokemons",
        "soma_niveis",
        "pontuacao"
    ]

    with open(
        caminho_saida,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

    print(f"\nArquivo gerado com sucesso: {caminho_saida.name}")
    print(f"Quantidade de resultados: {len(resultados)}")


def main():
    treinadores = carregar_csv("treinadores.csv")
    pokemons = carregar_csv("pokemons.csv")

    if not treinadores or not pokemons:
        print("Verifique se os arquivos CSV existem e possuem dados.")
        return

    resultados = []

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
            consultar_equipe(treinadores, pokemons)

        elif opcao == "3":
            resultados = calcular_pontuacoes(treinadores, pokemons)
            mostrar_pontuacoes(resultados)

        elif opcao == "4":
            if not resultados:
                resultados = calcular_pontuacoes(treinadores, pokemons)

            mostrar_classificacao(resultados)

        elif opcao == "5":
            if not resultados:
                resultados = calcular_pontuacoes(treinadores, pokemons)

            gerar_csv(resultados)

        elif opcao == "6":
            print("Encerrando o Campeonato Pokémon. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
