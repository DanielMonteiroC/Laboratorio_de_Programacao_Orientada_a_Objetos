class Banco():
    def __init__(self,nome,endereco,agencia):
        self.nome = nome
        self.endereco = endereco
        self.agencia = agencia
        self.clientes = []

    def imprime_nome_banco(self):
        print(f'O nome do banco é: {self.nome} \n'
              f'O endereço do banco é: {self.endereco} \n'
              f'A agencia do banco é: {self.agencia}')

    def adicionar_clientes(self,cliente):
        self.clientes.append(cliente)

    def listar_cliente(self):
        for cliente in self.clientes:
            print(cliente)