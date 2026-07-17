numero = int(input("Digite um número positivo: "))

while numero <= 0:
    print("Entrada inválida. Digite um número positivo.")
    numero = int(input("Digite um número positivo: "))

print("Número válido:", numero)