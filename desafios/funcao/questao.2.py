def maior(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("O maior número é:", maior(a, b))