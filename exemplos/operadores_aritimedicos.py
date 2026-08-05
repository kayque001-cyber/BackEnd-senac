'''
operadores     função
_________________________________
+               soma
-               subtração
*               multiplicação
/               divisão
//              divisão inteira
%               resto
**              potência
_________________________________
'''

numero1 = 10
numero2 = 3
#soma
soma = numero1+numero2
print(f"soma: {numero1+numero2}")#soma
print(f"soma: {soma}")
#print("Bruno"+"Gomes")


#subitração
print(f"soma: {numero1-numero2}")#subitração

#multiplicação
print(f"operação: {numero1*numero2}")

#divisão
print(f"operação: {numero1/numero2}")


#divisão inteira
print(f"operação: {numero1//numero2}")


#resto
print(f"operação: {numero1%numero2}")


#potência
print(f"operação: {numero1**numero2}")




numero = int(input("Digite um número: "))

fatorial = 1
conta = ""

print(f"\n{numero}! =\n")

for i in range(1, numero + 1):
    fatorial *= i

    if conta == "":
        conta = str(i)
    else:
        conta += f" x {i}"

    print(conta)

print(f"\nResultado = {fatorial}")