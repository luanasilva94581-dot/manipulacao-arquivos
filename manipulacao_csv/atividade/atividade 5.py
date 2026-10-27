
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


arquivo_pokemons = localizar_arquivo("pokemons.csv")
arquivo_treinadores = localizar_arquivo("treinadores.csv")

pokemons = []
treinadores = []

# Ler os arquivos CSV
if arquivo_pokemons is None or arquivo_treinadores is None:
    print("Erro: não foi possível encontrar os arquivos CSV.")
    print("Verifique se pokemons.csv e treinadores.csv estão no projeto.")

else:
    with open(arquivo_pokemons, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for pokemon in leitor:
            pokemons.append({
                "nome": pokemon["nome"].strip(),
                "tipo": pokemon["tipo"].strip(),
                "nivel": pokemon["nivel"].strip(),
                "treinador": pokemon["treinador"].strip()
            })

    with open(arquivo_treinadores, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for treinador in leitor:
            treinadores.append(treinador["nome"].strip())


    # Opção 1 - Listar Pokémon
    def listar_pokemons():
        if not pokemons:
            print("Nenhum Pokémon cadastrado.")
            return

        print("\n--- POKÉMON CADASTRADOS ---")

        for pokemon in pokemons:
            print("Nome:", pokemon["nome"])
            print("Tipo:", pokemon["tipo"])
            print("Nível:", pokemon["nivel"])
            print("Treinador:", pokemon["treinador"])
            print()


    # Opção 2 - Pesquisar Pokémon
    def pesquisar_pokemon():
        nome_busca = input("Digite o nome do Pokémon: ").strip()

        for pokemon in pokemons:
            if pokemon["nome"].lower() == nome_busca.lower():
                print("\nNome:", pokemon["nome"])
                print("Tipo:", pokemon["tipo"])
                print("Nível:", pokemon["nivel"])
                print("Treinador:", pokemon["treinador"])
                return

        print("Pokémon não encontrado.")


    # Opção 3 - Adicionar Pokémon
    def adicionar_pokemon():
        nome = input("Nome: ").strip()

        if nome == "":
            print("O nome não pode ficar vazio.")
            return

        # Verificar se o Pokémon já existe
        for pokemon in pokemons:
            if pokemon["nome"].lower() == nome.lower():
                print("Esse Pokémon já está cadastrado.")
                return

        tipo = input("Tipo: ").strip()

        if tipo == "":
            print("O tipo não pode ficar vazio.")
            return

        nivel = input("Nível: ").strip()

        if not nivel.isdigit():
            print("O nível deve ser um número inteiro.")
            return

        nivel_numero = int(nivel)

        if nivel_numero < 1 or nivel_numero > 100:
            print("O nível deve estar entre 1 e 100.")
            return

        treinador = input("Treinador: ").strip()

        treinador_encontrado = None

        for nome_treinador in treinadores:
            if nome_treinador.lower() == treinador.lower():
                treinador_encontrado = nome_treinador
                break

        if treinador_encontrado is None:
            print("Treinador não encontrado.")
            return

        novo_pokemon = {
            "nome": nome,
            "tipo": tipo,
            "nivel": str(nivel_numero),
            "treinador": treinador_encontrado
        }

        pokemons.append(novo_pokemon)

        print("Pokémon adicionado com sucesso!")
        print("Não esqueça de salvar as alterações na opção 6.")


    # Opção 4 - Alterar nível
    def alterar_nivel():
        nome_busca = input("Digite o nome do Pokémon: ").strip()

        for pokemon in pokemons:
            if pokemon["nome"].lower() == nome_busca.lower():
                novo_nivel = input("Digite o novo nível: ").strip()

                if not novo_nivel.isdigit():
                    print("O nível deve ser um número inteiro.")
                    return

                nivel_numero = int(novo_nivel)

                if nivel_numero < 1 or nivel_numero > 100:
                    print("O nível deve estar entre 1 e 100.")
                    return

                pokemon["nivel"] = str(nivel_numero)

                print("Nível alterado com sucesso!")
                print("Não esqueça de salvar as alterações na opção 6.")
                return

        print("Pokémon não encontrado.")


    # Opção 5 - Remover Pokémon
    def remover_pokemon():
        nome_busca = input("Digite o nome do Pokémon: ").strip()

        for pokemon in pokemons:
            if pokemon["nome"].lower() == nome_busca.lower():
                pokemons.remove(pokemon)
                print("Pokémon removido com sucesso!")
                print("Não esqueça de salvar as alterações na opção 6.")
                return

        print("Pokémon não encontrado.")


    # Opção 6 - Salvar alterações
    def salvar_alteracoes():
        caminho_saida = pasta_atual / "pokemons_atualizados.csv"

        colunas = ["nome", "tipo", "nivel", "treinador"]

        with open(
            caminho_saida,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=colunas
            )

            escritor.writeheader()
            escritor.writerows(pokemons)

        print("Alterações salvas com sucesso!")
        print("Arquivo:", caminho_saida.name)
        print("Quantidade de Pokémon gravados:", len(pokemons))


    # Menu principal
    while True:
        print("\n===== GERENCIADOR DE POKÉMON =====")
        print("1 - Listar Pokémon")
        print("2 - Pesquisar Pokémon")
        print("3 - Adicionar Pokémon")
        print("4 - Alterar nível de um Pokémon")
        print("5 - Remover Pokémon")
        print("6 - Salvar alterações")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_pokemons()

        elif opcao == "2":
            pesquisar_pokemon()

        elif opcao == "3":
            adicionar_pokemon()

        elif opcao == "4":
            alterar_nivel()

        elif opcao == "5":
            remover_pokemon()

        elif opcao == "6":
            salvar_alteracoes()

        elif opcao == "7":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
