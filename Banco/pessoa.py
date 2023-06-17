class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def __str__(self):
        return f'Nome: {self.__nome} {self.__sobrenome}\n CPF: {self.__cpf}'
        
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, banco):
        super().__init__(nome, sobrenome, cpf)
        self.banco = banco
