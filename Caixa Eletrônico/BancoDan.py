#codigo classe conta (sacar, depositar, transferir, exibir)

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente.')
            print('*'*89)
        else:
            print(f'Saque no valor de R${valor} realizado com sucesso.')
            self.saldo -= valor
            print('*'*89)

    def deposito(self, valor):
        if valor <= 0:
            print('O valor mínimo de depósito é R$ 0,01, por favor tente novamente.')
            print('*'*89)
        else:
            print(f'Você depositou R$ {valor} na conta de {self.titular} com sucesso.')
            print('*'*89)
            self.saldo += valor

    def transferencia(self, destino, valor):
        if valor >= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f'Você transferiu R${valor} para {destino.titular} com sucesso.')
            print('*'*89)
        else:
            print(f'Você não possui saldo o suficiente.')

    def extrato(self):
        print('EXTRATO SIMPLIFICADO')
        print(f'Titular: {self.titular}\n'
              f'Conta: {self.numero}\n'
              f'Saldo: {self.saldo}\n'
              f'Limite Disponível: {self.limite}\n')
        print('*'*89)