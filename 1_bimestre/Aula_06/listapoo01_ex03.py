class Conta:
    def __init__(self):
        self.nome = 'João Fulano nao sei quem'
        self.numero = 2432
        self.saldo = 1500
    def saque(self, valor):
        self.saldo -= valor
        return self.saldo
    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

x = Conta()
x.nome = 'Jose'
x.numero = 1
x.saldo = 1500
print(x.saque(300))
print(x.deposito(3000))