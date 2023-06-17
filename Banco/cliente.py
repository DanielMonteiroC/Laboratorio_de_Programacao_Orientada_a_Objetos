class Cliente():
    proximo_id = 1
    def __init__(self,nome,sobrenome,cpf,banco):
        self.id = Cliente.proximo_id
        Cliente.proximo_id += 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.banco = banco

    def __str__(self):
        return (f'Cliente ID: {self.id} \n'
                f'Nome completo: {self.__nome} {self.__sobrenome}\n'
                f'CPF: {self.__cpf}\n'
                f'========================================')