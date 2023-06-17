from conta import *
from cliente import *
from banco import *

if __name__ == '__main__':
    banco = Banco('Bamerindus', 'Céu', '8888')
    cliente1 = Cliente('Daniel', 'Monteiro', '131456879-14',banco)
    conta1 = Conta('2345', cliente1, 100)
    cliente2 = Cliente('Carlos','Alberto','131548697-41',banco)
    conta2 = Conta('6780',cliente2,1000)

    print(conta1.transfere_para(50,conta2))
    print(conta2.saldo)
    print('='*40)
    conta1.saque(60)
    conta1.deposito(80)
    conta1.historico.imprime_transacoes()
    print("="*40)
    print(conta1.titular)
    print('='*40)
    print("Banco Banerj")

    banco.adicionar_clientes(cliente1)
    banco.adicionar_clientes(cliente2)
    banco.listar_cliente()
    print("="*101)
    print(cliente2.banco.agencia)