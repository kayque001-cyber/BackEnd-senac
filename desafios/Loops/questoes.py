def entrada_valida():

    while True:

        numero = int(input("Digite um número positivo: "))

        if numero > 0:
            print("Número válido!")
            break

        print("Número inválido! Tente novamente.")


def soma_acumulada():

    soma = 0

    while True:

        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break

        soma += numero

    print("Soma total:", soma)


def mostrar_pares():

    print()

    for numero in range(1, 21):

        if numero % 2 == 0:
            print(numero)


def soma_ate_zero():

    soma = 0

    while True:

        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break

        soma += numero

    print("Soma:", soma)


def pares_ate_cinquenta():

    print()

    for numero in range(0, 51, 2):
        print(numero)


def validar_senha():

    while True:

        senha = input("Digite a senha: ")

        if senha == "senha123":
            print("Senha correta!")
            break

        print("Senha incorreta!")


def somar_positivos():

    lista = [-1, 2, -3, 4]

    soma = 0

    for numero in lista:

        if numero < 0:
            continue

        soma += numero

    print("Soma dos positivos:", soma)


def contador_regressivo():

    print()

    for numero in range(10, 0, -1):
        print(numero)


def menu():

    while True:

        print("\n===================================")
        print(" SISTEMA DE EXERCÍCIOS - LOOPS ")
        print("===================================")
        print("1 - Entrada Válida")
        print("2 - Soma Acumulada")
        print("3 - Mostrar Pares (1 a 20)")
        print("4 - Soma até Zero")
        print("5 - Pares até 50")
        print("6 - Validar Senha")
        print("7 - Somar Positivos")
        print("8 - Contador Regressivo")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                entrada_valida()

            case "2":
                soma_acumulada()

            case "3":
                mostrar_pares()

            case "4":
                soma_ate_zero()

            case "5":
                pares_ate_cinquenta()

            case "6":
                validar_senha()

            case "7":
                somar_positivos()

            case "8":
                contador_regressivo()

            case "0":
                print("Sistema encerrado.")
                break

            case _:
                print("Opção inválida!")


menu()