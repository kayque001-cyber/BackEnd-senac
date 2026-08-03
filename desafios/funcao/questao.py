def verificar_par():
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


def maior_numero():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a > b:
        print("Maior número:", a)
    else:
        print("Maior número:", b)


def fatorial():
    n = int(input("Digite um número: "))

    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    print("Fatorial:", resultado)


def contar():
    n = int(input("Digite um número: "))

    contador = 1

    while contador <= n:
        print(contador)
        contador += 1


def soma_ate_zero():
    soma = 0

    while True:
        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break

        soma += numero

    print("Soma:", soma)


def calculadora():
    while True:

        print("\n1 - Somar")
        print("2 - Subtrair")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            a = int(input("Primeiro número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", a + b)

        elif opcao == "2":
            a = int(input("Primeiro número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", a - b)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def validar_senha():

    while True:
        senha = input("Digite a senha: ")

        if senha == "python123":
            print("Senha correta!")
            break

        print("Senha incorreta.")


def contar_pares():
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))

    quantidade = 0

    for numero in range(inicio, fim + 1):

        if numero % 2 == 0:
            quantidade += 1

    print("Quantidade de pares:", quantidade)


def tabuada():
    numero = int(input("Digite um número: "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def tres_tentativas():

    tentativas = 0

    while tentativas < 3:

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "1234":
            print("Login realizado!")
            return

        tentativas += 1
        print("Login inválido.")

    print("Número de tentativas excedido.")


def impares_sem_multiplos7():

    limite = int(input("Digite o limite: "))

    for numero in range(1, limite + 1):

        if numero % 7 == 0:
            continue

        if numero % 2 != 0:
            print(numero)


def menu():

    while True:

        print("\n===================================")
        print(" SISTEMA DE EXERCÍCIOS - FUNÇÕES ")
        print("===================================")
        print("1  - Verificar Par ou Ímpar")
        print("2  - Maior Número")
        print("3  - Fatorial")
        print("4  - Contar até N")
        print("5  - Soma até Zero")
        print("6  - Calculadora")
        print("7  - Validar Senha")
        print("8  - Contar Pares")
        print("9  - Tabuada")
        print("10 - Três Tentativas de Login")
        print("11 - Ímpares sem Múltiplos de 7")
        print("0  - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                verificar_par()

            case "2":
                maior_numero()

            case "3":
                fatorial()

            case "4":
                contar()

            case "5":
                soma_ate_zero()

            case "6":
                calculadora()

            case "7":
                validar_senha()

            case "8":
                contar_pares()

            case "9":
                tabuada()

            case "10":
                tres_tentativas()

            case "11":
                impares_sem_multiplos7()

            case "0":
                print("Sistema encerrado.")
                break

            case _:
                print("Opção inválida!")


menu()