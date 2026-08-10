class Banco:
    def __init__(self, saldo=0):
        self.saldo = saldo

    @property
    def saldo_E50(self):
        return self.saldo

    def depositar(self, valor):
        if valor <=0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor


    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor



banco_master = Banco(100)
banco_master.depositar(150)
banco_master.sacar(50)
banco_master.saldo_E50


class Conta(Banco):
    def __init__(self, num_conta, cliente, saldo=0, agencia=455):
        super().__init__(saldo)
        self.num_conta = num_conta
        self.cliente = cliente
        self.agencia = agencia

    def __str__(self):
        return f"Conta: {self.num_conta}, Cliente: {self.cliente}, Saldo: {self.saldo}, Agência: {self.agencia}"

conta1 = Conta("1111111-1", "João", banco_master.saldo_E50, 455)



print(
    f"Agência: {conta1.agencia} | "
    f"Saldo atual: R${conta1.saldo:.2f} | "
    f"Número da Conta: {conta1.num_conta} | "
    f"Cliente: {conta1.cliente}"
)