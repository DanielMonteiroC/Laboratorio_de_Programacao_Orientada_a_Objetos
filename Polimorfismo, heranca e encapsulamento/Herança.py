# A herança permite a criação de hierarquias de classes, facilitando a reutilização de código 
# e a organização lógica do programa.


# Aqui, definimos a classe base chamada "Veiculo". Ela possui um construtor __init__ que recebe 
# os parâmetros e os atribui aos atributos da classe. Também possui os métodos ligar() e 
# desligar() que imprimem mensagens indicando o estado do veículo.
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veículo está ligado.")

    def desligar(self):
        print("O veículo está desligado.")

# Definimos a classe derivada "Carro" que herda da classe base "Veiculo". Ela também possui um 
# construtor __init__, que utiliza a função super() para chamar o construtor da classe base e 
# atribuir os valores. Além disso, a classe "Carro" adiciona um novo atributo. Ela possui o 
# método dirigir(), que imprime uma mensagem indicando o movimento do carro.
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def dirigir(self):
        print(f"O carro {self.marca} {self.modelo} de cor {self.cor} está em movimento.")

# Definimos a classe derivada "Moto" que inicialmente faz o mesmo que a classe derivada "Carro".
# A classe "Moto" também adiciona um novo atributo. Ela possui o método acelerar(), que imprime 
# uma mensagem indicando a aceleração da moto.
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def acelerar(self):
        print(f"A moto {self.marca} {self.modelo} com {self.cilindrada}cc está acelerando.")


# Nesta parte do código, criamos instâncias das classes derivadas "Carro" e "Moto" usando o 
# construtor de cada classe, passando os argumentos apropriados.
carro = Carro("Ford", "Mustang", "vermelho")
moto = Moto("Honda", "CBR 1000RR", 1000)

# Em seguida, chamamos os métodos específicos de cada classe, como carro.dirigir() e 
# moto.acelerar(), além de chamar os métodos herdados da classe base, como carro.ligar() e 
# moto.desligar().
carro.ligar()
carro.dirigir()
carro.desligar()

moto.ligar()
moto.acelerar()
moto.desligar()

# Esse exemplo ilustra como a herança permite que as classes derivadas herdem atributos e 
# métodos da classe base, além de adicionar comportamentos específicos ou substituir os 
# comportamentos herdados. Isso promove a reutilização de código e a organização lógica do 
# programa.