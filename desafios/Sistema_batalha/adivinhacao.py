def menu():
    print("====Adivinhe o Número====")

while True:
    menu()
    print()
    numero = int(input("Digite o Número: \n"))

    def numero_aleatorio():
        import random
        return random.randint(1, 100)

    if numero == numero_aleatorio():
        print("Parabéns! Você acertou o número!")
        break
    elif numero <= numero_aleatorio():
        print("O número é maior! Tente novamente.")
        numero = int(input("Digite o Número: "))
    else:
        print("O número é menor! Tente novamente.")
        numero = int(input("Digite o Número: "))