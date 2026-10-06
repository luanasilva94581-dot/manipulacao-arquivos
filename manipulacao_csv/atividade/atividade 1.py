import csv


# Carregar os treinadores do arquivo CSV
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


# Menu principal
def menu():
    treinadores = carregar_treinadores()

    while True:
        print("\n===== TREINADORES POKÉMON =====")
        print("1 - Listar todos os treinadores")
        print("2 - Buscar treinador pelo nome")
        print("3 - Listar treinadores de uma região")
        print("4 - Mostrar treinador com maior nível")
        print("5 - Mostrar treinador com menor nível")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        # 1 - Listar todos
        if opcao == "1":

            if not treinadores:
                print("Nenhum treinador encontrado.")
            else:
                for treinador in treinadores:
                    print(
                        f"Nome: {treinador['nome']}, "
                        f"Região: {treinador['regiao']}, "
                        f"Nível: {treinador['nivel']}"
                    )

        # 2 - Buscar pelo nome
        elif opcao == "2":

            nome = input("Digite o nome do treinador: ").strip().lower()

            encontrado = False

            for treinador in treinadores:
                if treinador["nome"].lower() == nome:
                    print("\nTreinador encontrado!")
                    print(f"Nome: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")

                    encontrado = True
                    break

            if not encontrado:
                print("Treinador não encontrado.")

        # 3 - Listar por região
        elif opcao == "3":

            regiao = input("Digite a região: ").strip().lower()

            encontrados = []

            for treinador in treinadores:
                if treinador["regiao"].lower() == regiao:
                    encontrados.append(treinador)

            if encontrados:
                print(f"\nTreinadores da região {regiao.title()}:")

                for treinador in encontrados:
                    print(
                        f"Nome: {treinador['nome']} - "
                        f"Nível: {treinador['nivel']}"
                    )
            else:
                print("Nenhum treinador encontrado nessa região.")

        # 4 - Maior nível
        elif opcao == "4":

            if treinadores:
                maior = max(
                    treinadores,
                    key=lambda treinador: int(treinador["nivel"])
                )

                print(
                    f"\nTreinador com maior nível: "
                    f"{maior['nome']} - Nível {maior['nivel']}"
                )
            else:
                print("Nenhum treinador encontrado.")

        # 5 - Menor nível
        elif opcao == "5":

            if treinadores:
                menor = min(
                    treinadores,
                    key=lambda treinador: int(treinador["nivel"])
                )

                print(
                    f"\nTreinador com menor nível: "
                    f"{menor['nome']} - Nível {menor['nivel']}"
                )
            else:
                print("Nenhum treinador encontrado.")

        # 6 - Sair
        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()