class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno:

    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(f"{self.nome} está estudando.")


class Contador:

    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor += 1

    def diminuir(self):
        self.valor -= 1


class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


class Livro:

    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True


class Veiculo:

    def __init__(self, marca):
        self.marca = marca


class Carro(Veiculo):

    def __init__(self, marca):
        super().__init__(marca)


class Moto(Veiculo):

    def __init__(self, marca):
        super().__init__(marca)


class Agenda:

    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome):
        self.contatos.append(nome)


class Usuario:

    quantidade = 0

    def __init__(self, nome):
        self.nome = nome
        Usuario.quantidade += 1


# ==============================
# Exercícios
# ==============================

def exercicio_pessoa():

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    pessoa = Pessoa(nome, idade)

    print("\nDados da Pessoa")
    print("Nome:", pessoa.nome)
    print("Idade:", pessoa.idade)


def exercicio_aluno():

    nome = input("Nome do aluno: ")

    aluno = Aluno(nome)

    aluno.estudar()


def exercicio_contador():

    contador = Contador()

    contador.aumentar()
    contador.aumentar()
    contador.diminuir()

    print("Valor do contador:", contador.valor)


def exercicio_produto():

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    desconto = float(input("Desconto (%): "))

    produto = Produto(nome, preco)

    produto.aplicar_desconto(desconto)

    print("Preço com desconto:", produto.preco)


def exercicio_livro():

    titulo = input("Título do livro: ")

    livro = Livro(titulo)

    print("Título:", livro.titulo)
    print("Disponível:", livro.disponivel)


def exercicio_veiculo():

    carro = Carro("Toyota")
    moto = Moto("Honda")

    print("Carro:", carro.marca)
    print("Moto:", moto.marca)


def exercicio_agenda():

    agenda = Agenda()

    agenda.adicionar_contato("João")
    agenda.adicionar_contato("Maria")
    agenda.adicionar_contato("Carlos")

    print("Contatos:")

    for contato in agenda.contatos:
        print(contato)


def exercicio_contador_objetos():

    Usuario.quantidade = 0

    Usuario("João")
    Usuario("Maria")
    Usuario("Carlos")

    print("Objetos criados:", Usuario.quantidade)


# ==============================
# Menu
# ==============================

def menu():

    while True:

        print("\n=================================")
        print(" SISTEMA DE EXERCÍCIOS - POO ")
        print("=================================")
        print("1 - Classe Pessoa")
        print("2 - Classe Aluno")
        print("3 - Classe Contador")
        print("4 - Classe Produto")
        print("5 - Classe Livro")
        print("6 - Herança (Carro e Moto)")
        print("7 - Classe Agenda")
        print("8 - Contador de Objetos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                exercicio_pessoa()

            case "2":
                exercicio_aluno()

            case "3":
                exercicio_contador()

            case "4":
                exercicio_produto()

            case "5":
                exercicio_livro()

            case "6":
                exercicio_veiculo()

            case "7":
                exercicio_agenda()

            case "8":
                exercicio_contador_objetos()

            case "0":
                print("Sistema encerrado.")
                break

            case _:
                print("Opção inválida!")


menu()