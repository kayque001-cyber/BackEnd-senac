def lista_cores():
    cores = ["Vermelho", "Azul", "Verde", "Amarelo"]

    print("\nLista de cores:")
    print(cores)


def primeiro_ultimo_numero():
    numeros = [10, 20, 30, 40, 50]

    print("\nPrimeiro número:", numeros[0])
    print("Último número:", numeros[-1])


def adicionar_nome():
    nomes = ["Ana", "Carlos", "Maria"]

    nomes.append("João")

    print("\nLista atualizada:")
    print(nomes)


def substituir_linguagem():
    linguagens = ["Python", "Java", "C#", "PHP"]

    linguagens[3] = "JavaScript"

    print("\nLista atualizada:")
    print(linguagens)


def remover_numero():
    numeros = [5, 10, 15, 20, 25]

    numeros.remove(15)

    print("\nLista final:")
    print(numeros)


def percorrer_lista():
    numeros = [1, 2, 3, 4, 5]

    print()

    for numero in numeros:
        print(numero)


def verificar_nome():
    nomes = ["Ana", "Carlos", "Maria", "João"]

    if "Maria" in nomes:
        print("\nNome encontrado!")
    else:
        print("\nNome não encontrado!")


def ordenar_lista():
    numeros = [50, 10, 80, 20, 40]

    numeros.sort()

    print("\nLista em ordem crescente:")
    print(numeros)


def tres_primeiros():
    numeros = [100, 200, 300, 400, 500]

    print("\nTrês primeiros elementos:")
    print(numeros[:3])


def cadastrar_numeros():
    numeros = []

    print()

    for i in range(5):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    print("\nLista completa:")
    print(numeros)

    print("Soma:", sum(numeros))


def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DE EXERCÍCIOS - LISTAS")
        print("==============================")
        print("1  - Lista de Cores")
        print("2  - Primeiro e Último Número")
        print("3  - Adicionar Nome")
        print("4  - Substituir Linguagem")
        print("5  - Remover Número")
        print("6  - Percorrer Lista")
        print("7  - Verificar Nome")
        print("8  - Ordenar Lista")
        print("9  - Fatiamento")
        print("10 - Cadastrar 5 Números")
        print("0  - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                lista_cores()

            case "2":
                primeiro_ultimo_numero()

            case "3":
                adicionar_nome()

            case "4":
                substituir_linguagem()

            case "5":
                remover_numero()

            case "6":
                percorrer_lista()

            case "7":
                verificar_nome()

            case "8":
                ordenar_lista()

            case "9":
                tres_primeiros()

            case "10":
                cadastrar_numeros()

            case "0":
                print("\nSistema encerrado.")
                break

            case _:
                print("Opção inválida!")


menu()