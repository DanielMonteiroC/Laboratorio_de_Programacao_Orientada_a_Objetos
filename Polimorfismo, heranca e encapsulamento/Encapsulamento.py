# O encapsulamento permite esconder os detalhes internos de uma classe, proteger os dados e 
# fornecer uma interface controlada para interagir com os objetos. Isso promove a modularidade, 
# proteção de dados e facilita a manutenção e extensibilidade do código.


# O método __init__ é o construtor da classe. Ele recebe o número da conta e o saldo inicial 
# como parâmetros e os atribui aos atributos privados __numero_conta e __saldo.
class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial):
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial
        
# O método depositar recebe um valor como parâmetro e o adiciona ao saldo atual da conta.
    def depositar(self, valor):
        self.__saldo += valor

# O método sacar recebe um valor como parâmetro, verifica se o saldo é suficiente para efetuar 
# o saque. Se o saldo for suficiente, o valor é subtraído do saldo atual da conta. Caso 
# contrário, é exibida uma mensagem informando que o saldo é insuficiente.
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")
        
# O método get_saldo retorna o saldo atual da conta.
    def get_saldo(self):
        return self.__saldo
        
# Criando uma instância da classe ContaBancaria.
conta = ContaBancaria("12345", 1000)

# Acessa indiretamente o atributo privado __numero_conta usando a convenção 
# _NomeClasse__nome_atributo.
print(conta._ContaBancaria__numero_conta)

# Altera indiretamente o atributo privado __saldo usando a convenção _NomeClasse__nome_atributo.
conta._ContaBancaria__saldo = 2000

print(conta.get_saldo())

conta.depositar(500)

conta.sacar(300)

print(conta.get_saldo())

