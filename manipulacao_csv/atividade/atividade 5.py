import csv

def carregar_dados():
    treinadores = []
    pokemons = []
    try:
        with open('treinadores.csv', mode='r', encoding='utf-8') as f:
            treinadores = list(csv.DictReader(f))
    except FileNotFoundError:
        print("Aviso: treinadores.csv não encontrado.")

    try:
        with open('pokemons.csv', mode='r', encoding='utf-8') as f:
            pokemons = list(csv.DictReader(f))
    except FileNotFoundError:
        print("Aviso: pokemons.csv não encontrado.")

    return treinadores, pokemons


def menu():
    treinadores, pokemons = carregar_dados()

    while True:
        print("\n===== GERENCIADOR DE POKÉMON =====")
        print("1 - Listar Pokémon")
        print("2 - Pesquisar Pokémon")
        print("3 - Adicionar Pokémon")
        print("4 - Alterar nível de um Pokémon")
        print("5 - Remover Pokémon")
        print("6 - Salvar alterações")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for p in pokemons:
                print(
                    f"Nome: {p.get('nome')}, Tipo: {p.get('tipo')}, Nível: {p.get('nivel')}, Treinador: {p.get('treinador')}")

        elif opcao == "2":
            nome = input("Digite o nome do Pokémon: ").strip().lower()
            p_encontrado = next((p for p in pokemons if p.get('nome', '').lower() == nome), None)
            if p_encontrado:
                print(f"Nome: {p_encontrado.get('nome')}")
                print(f"Tipo: {p_encontrado.get('tipo')}")
                print(f"Nível: {p_encontrado.get('nivel')}")
                print(f"Treinador: {p_encontrado.get('treinador')}")
            else:
                print("Pokémon não encontrado.")

        elif opcao == "3":
            nome = input("Nome: ").strip()
            tipo = input("Tipo: ").strip()
            nivel_str = input("Nível (1-100): ").strip()
            treinador = input("Treinador: ").strip()

            # Validações
            if not nome or not tipo:
                print("Erro: Nome e Tipo não podem ser vazios.")
                continue
            try:
                nivel = int(nivel_str)
                if nivel < 1 or nivel > 100:
                    print("Erro: O nível deve estar entre 1 e 100.")
                    continue
            except ValueError:
                print("Erro: Nível inválido.")
                continue

            # Validar se treinador existe
            treinador_existe = any(t.get('nome', '').lower() == treinador.lower() for t in treinadores)
            if not treinador_existe:
                print("Erro: O treinador informado não existe em treinadores.csv.")
                continue

            # Validar duplicado
            if any(p.get('nome', '').lower() == nome.lower() for p in pokemons):
                print("Erro: Este Pokémon já está cadastrado.")
                continue

            novo_p = {
                "nome": nome,
                "tipo": tipo,
                "nivel": str(nivel),
                "treinador": treinador
            }
            pokemons.append(novo_p)
            print("Pokémon adicionado à lista local!")

        elif opcao == "4":
            nome = input("Digite o nome do Pokémon a alterar: ").strip().lower()
            p_encontrado = next((p for p in pokemons if p.get('nome', '').lower() == nome), None)
            if p_encontrado:
                try:
                    novo_nivel = int(input("Digite o novo nível (1-100): "))
                    if 1 <= novo_nivel <= 100:
                        p_encontrado['nivel'] = str(novo_nivel)
                        print("Nível alterado com sucesso!")
                    else:
                        print("Nível inválido.")
                except ValueError:
                    print("Valor inválido.")
            else:
                print("Pokémon não encontrado.")

        elif opcao == "5":
            nome = input("Digite o nome do Pokémon a remover: ").strip().lower()
            p_encontrado = next((p for p in pokemons if p.get('nome', '').lower() == nome), None)
            if p_encontrado:
                pokemons.remove(p_encontrado)
                print("Pokémon removido da lista local!")
            else:
                print("Pokémon não encontrado.")

        elif opcao == "6":
            with open('pokemons_atualizados.csv', mode='w', newline='', encoding='utf-8') as f:
                campos = ['nome', 'tipo', 'nivel', 'treinador']
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                for p in pokemons:
                    escritor.writerow({
                        'nome': p.get('nome'),
                        'tipo': p.get('tipo'),
                        'nivel': p.get('nivel'),
                        'treinador': p.get('treinador')
                    })
            print("Alterações salvas em 'pokemons_atualizados.csv'!")

        elif opcao == "7":
            print("A sair...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()