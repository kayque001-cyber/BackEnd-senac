total = 0

numero = int(input("Digite um valor (0 para sair): "))

while numero != 0:
    total += numero
    numero = int(input("Digite um valor (0 para sair): "))

print("Total da soma:", total)