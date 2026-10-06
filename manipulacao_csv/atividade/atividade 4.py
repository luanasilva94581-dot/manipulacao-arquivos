import csv

def carregar_dados():
    try:
        with open('treinadores.csv', mode='r', encoding='utf-8') as f:
            treinadores = list(csv.DictReader(f))
        with open('pokemons.csv', mode='r', encoding='utf-8') as f:
            pokemons = list(csv.DictReader(f))
        return treinadores, pokemons
    except FileNotFoundError as e:
        print(f"Erro ao carregar ficheiro: {e}")
        return [], []


def menu():
    treinadores, pokemons = carregar_dados()

    while True:
        print("\n===== GERADOR DE ARQUIVOS =====")
        print("1 - Listar treinadores")
        print("2 - Gerar CSV de um treinador")
        print("3 - Gerar CSV de todos os treinadores (ordenados por nível)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for t in treinadores:
                print(f"Nome: {t.get('nome')}")

        elif opcao == "2":
            nome_input = input("Digite o treinador: ").strip()
            poks_filtrados = [p for p in pokemons if p.get('treinador', '').lower() == nome_input.lower()]

            if not poks_filtrados:
                print("Nenhum Pokémon encontrado para este treinador.")
                continue

            nome_arquivo = f"pokemons_{nome_input.lower().replace(' ', '_')}.csv"

            with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as f:
                campos = ['nome', 'tipo', 'nivel', 'treinador']
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                for p in poks_filtrados:
                    escritor.writerow({
                        'nome': p.get('nome'),
                        'tipo': p.get('tipo'),
                        'nivel': p.get('nivel'),
                        'treinador': p.get('treinador')
                    })
            print(f"Ficheiro {nome_arquivo} gerado com sucesso! Registos gravados: {len(poks_filtrados)}")

        elif opcao == "3":
            nome_arquivo = "todos_pokemons_ordenados.csv"
            pokemons_ordenados = sorted(pokemons, key=lambda p: int(p.get('nivel', 0)), reverse=True)

            with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as f:
                campos = ['nome', 'tipo', 'nivel', 'treinador']
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                for p in pokemons_ordenados:
                    escritor.writerow({
                        'nome': p.get('nome'),
                        'tipo': p.get('tipo'),
                        'nivel': p.get('nivel'),
                        'treinador': p.get('treinador')
                    })
            print(f"Ficheiro {nome_arquivo} gerado com sucesso! Registos gravados: {len(pokemons_ordenados)}")

        elif opcao == "4":
            print("A sair...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()