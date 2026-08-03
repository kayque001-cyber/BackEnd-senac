def verificar_login():
    usuario = input("Digite o nome de usuário: ")

    if usuario == "admin":
        print("Acesso permitido")
    else:
        print("Acesso negado")


def verificar_idade():
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Acesso liberado ao sistema.")
    else:
        print("Acesso negado. Você precisa ter 18 anos ou mais para acessar o sistema.")

def aplicar_desconto():
    valor = float(input("Digite o valor da compra: R$ "))

    if valor > 100:
        print("Desconto aplicado!")
    else:
        print("Desconto não aplicado.")


def sistema_acesso():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "1234":
        print("Bem-vindo!")
    else:
        print("Usuário ou senha incorretos.")


def verificar_aprovacao():
    nota = float(input("Digite a nota do aluno: "))

    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


def verificar_estoque():
    estoque = int(input("Quantidade disponível: "))
    pedido = int(input("Quantidade pedida: "))

    if pedido > estoque:
        print("Estoque insuficiente.")
    else:
        print("Pedido confirmado.")


def verificar_par_impar():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


def verificar_conceito():
    nota = float(input("Digite a nota: "))

    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bom")
    elif nota >= 5:
        print("Regular")
    else:
        print("Insuficiente")


def verificar_dia_semana():
    dia = input("Digite um dia da semana: ").lower()

    match dia:
        case "segunda":
            print("Dia de semana")
        case "terça" | "terca":
            print("Dia de semana")
        case "quarta":
            print("Dia de semana")
        case "quinta":
            print("Dia de semana")
        case "sexta":
            print("Dia de semana")
        case "sábado" | "sabado":
            print("Final de semana")
        case "domingo":
            print("Final de semana")
        case _:
            print("Dia inválido!")


def menu_escolha():
    print("\n===== MENU DE ESCOLHA =====")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Opção 4")
    print("5 - Opção 5")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("Você escolheu a opção 1.")
        case 2:
            print("Você escolheu a opção 2.")
        case 3:
            print("Você escolheu a opção 3.")
        case 4:
            print("Você escolheu a opção 4.")
        case 5:
            print("Você escolheu a opção 5.")
        case _:
            print("Opção inválida!")


def menu():
    while True:
        print("\n===============================")
        print(" SISTEMA DE EXERCÍCIOS PYTHON ")
        print("===============================")
        print("1  - Verificar Login")
        print("2  - Verificar Idade")
        print("3  - Aplicar Desconto")
        print("4  - Sistema de Acesso")
        print("5  - Verificar Aprovação")
        print("6  - Verificar Estoque")
        print("7  - Verificar Par ou Ímpar")
        print("8  - Verificar Conceito")
        print("9  - Verificar Dia da Semana")
        print("10 - Menu de Escolha")
        print("0  - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                verificar_login()

            case "2":
                verificar_idade()

            case "3":
                aplicar_desconto()

            case "4":
                sistema_acesso()

            case "5":
                verificar_aprovacao()

            case "6":
                verificar_estoque()

            case "7":
                verificar_par_impar()

            case "8":
                verificar_conceito()

            case "9":
                verificar_dia_semana()

            case "10":
                menu_escolha()

            case "0":
                print("\nEncerrando o sistema...")
                break

            case _:
                print("Opção inválida! Tente novamente.")


menu()