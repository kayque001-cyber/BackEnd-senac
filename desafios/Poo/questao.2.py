class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(f"{self.nome} está estudando.")


aluno1 = Aluno("Kayque")


aluno1.estudar()