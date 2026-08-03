def criar_funcionario():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior"
    }

    print("\nFuncionário:")
    print(funcionario)


def acessar_dados():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior"
    }

    print("\nNome:", funcionario["nome"])
    print("Cargo:", funcionario["cargo"])


def adicionar_salario():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior"
    }

    funcionario["salario"] = 3500

    print("\nFuncionário atualizado:")
    print(funcionario)


def alterar_cargo():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior"
    }

    funcionario["cargo"] = "Pleno"

    print("\nFuncionário atualizado:")
    print(funcionario)


def percorrer_dicionario():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior"
    }

    print()

    for chave, valor in funcionario.items():
        print(f"{chave} -> {valor}")


def lista_funcionarios():
    funcionarios = [
        {"id": 1, "nome": "Valdir", "cargo": "Gerente"},
        {"id": 2, "nome": "José", "cargo": "Suporte"},
        {"id": 3, "nome": "Maria", "cargo": "Analista"}
    ]

    print()

    for funcionario in funcionarios:
        print(
            f"ID: {funcionario['id']:02d} - "
            f"Nome: {funcionario['nome']} - "
            f"Cargo: {funcionario['cargo']}"
        )


def atualizar_funcionario():
    funcionario = {
        "nome": "João",
        "idade": 25,
        "cargo": "Júnior",
        "salario": 3500
    }

    funcionario["cargo"] = "Sênior"
    funcionario["salario"] = 5000

    print("\nFuncionário atualizado:")
    print(funcionario)


def funcionario_input():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    setor = input("Setor: ")

    funcionario = {
        "nome": nome,
        "idade": idade,
        "setor": setor
    }

    print("\nFuncionário cadastrado:")
    print(funcionario)


def menu():
    while True:
        print("\n===================================")
        print(" SISTEMA DE EXERCÍCIOS - DICIONÁRIOS ")
        print("===================================")
        print("1 - Criar Funcionário")
        print("2 - Acessar Nome e Cargo")
        print("3 - Adicionar Salário")
        print("4 - Alterar Cargo")
        print("5 - Percorrer Dicionário")
        print("6 - Lista de Funcionários")
        print("7 - Atualizar Funcionário")
        print("8 - Cadastrar Funcionário")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                criar_funcionario()

            case "2":
                acessar_dados()

            case "3":
                adicionar_salario()

            case "4":
                alterar_cargo()

            case "5":
                percorrer_dicionario()

            case "6":
                lista_funcionarios()

            case "7":
                atualizar_funcionario()

            case "8":
                funcionario_input()

            case "0":
                print("\nSistema encerrado.")
                break

            case _:
                print("Opção inválida!")


menu()