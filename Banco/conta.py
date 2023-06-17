from historico import *
class Conta():
    def __init__(self,numero, cliente,saldo):
        self.agencia = cliente.banco.agencia
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.historico = Historico()

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {} efetuado com sucesso. Seu saldo atual é de {}".format(valor,self.saldo))


    def deposito(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {} efetuado com sucesso. Seu saldo atual é de {}.".format(valor,self.saldo))

    def transfere_para(self,valor,destino):
        self.saldo -= valor
        destino.saldo += valor
        return(f'Transferência de: {valor} efetuada com sucesso.\n'
              f'Conta de destino: {destino.numero}')

    def extrato(self):
        print(f'Titular: {self.titular} \n'
              f'Número: {self.numero} \n'
              f'Saldo atual: {self.saldo}')
