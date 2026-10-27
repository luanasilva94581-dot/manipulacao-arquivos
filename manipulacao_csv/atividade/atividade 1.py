
import csv
from pathlib import Path

treinadores = []

# Localizar o arquivo treinadores.csv
pasta_atual = Path(__file__).resolve().parent
arquivo_csv = None

for pasta in [pasta_atual, *pasta_atual.parents]:
    caminho = pasta / "treinadores.csv"

    if caminho.exists():
        arquivo_csv = caminho
        break

# Ler o arquivo CSV
if arquivo_csv is None:
    print("Erro: arquivo treinadores.csv não encontrado.")
    print("Coloque o arquivo na mesma pasta do código ou em uma pasta acima.")

else:
    with open(arquivo_csv, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for treinador in leitor:
            treinadores.append(treinador)


    def listar_treinadores():
        print("\n--- TODOS OS TREINADORES ---")

        for treinador in treinadores:
            print("Nome:", treinador["nome"])
            print("Região:", treinador["regiao"])
            print("Nível:", treinador["nivel"])
            print()


    def buscar_treinador():
        nome_busca = input("Digite o nome do treinador: ").strip()
        encontrado = False

        for treinador in treinadores:
            if treinador["nome"].strip().lower() == nome_busca.lower():
                print("\nNome:", treinador["nome"])
                print("Região:", treinador["regiao"])
                print("Nível:", treinador["nivel"])
                encontrado = True
                break

        if not encontrado:
            print("Treinador não encontrado.")


    def listar_por_regiao():
        regiao_busca = input("Digite a região: ").strip()
        encontrado = False

        for treinador in treinadores:
            if treinador["regiao"].strip().lower() == regiao_busca.lower():
                print("\nNome:", treinador["nome"])
                print("Região:", treinador["regiao"])
                print("Nível:", treinador["nivel"])
                encontrado = True

        if not encontrado:
            print("Nenhum treinador encontrado nessa região.")


    def mostrar_maior_nivel():
        if not treinadores:
            print("Não existem treinadores cadastrados.")
            return

        maior = treinadores[0]

        for treinador in treinadores:
            if int(treinador["nivel"]) > int(maior["nivel"]):
                maior = treinador

        print("\n--- TREINADOR COM MAIOR NÍVEL ---")
        print("Nome:", maior["nome"])
        print("Região:", maior["regiao"])
        print("Nível:", maior["nivel"])


    def mostrar_menor_nivel():
        if not treinadores:
            print("Não existem treinadores cadastrados.")
            return

        menor = treinadores[0]

        for treinador in treinadores:
            if int(treinador["nivel"]) < int(menor["nivel"]):
                menor = treinador

        print("\n--- TREINADOR COM MENOR NÍVEL ---")
        print("Nome:", menor["nome"])
        print("Região:", menor["regiao"])
        print("Nível:", menor["nivel"])


    while True:
        print("\n===== TREINADORES POKÉMON =====")
        print("1 - Listar todos os treinadores")
        print("2 - Buscar treinador pelo nome")
        print("3 - Listar treinadores de uma região")
        print("4 - Mostrar treinador com maior nível")
        print("5 - Mostrar treinador com menor nível")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_treinadores()

        elif opcao == "2":
            buscar_treinador()

        elif opcao == "3":
            listar_por_regiao()

        elif opcao == "4":
            mostrar_maior_nivel()

        elif opcao == "5":
            mostrar_menor_nivel()

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
