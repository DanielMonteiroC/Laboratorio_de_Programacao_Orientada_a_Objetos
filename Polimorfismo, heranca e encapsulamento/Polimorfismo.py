# O polimorfismo permite que os objetos das classes derivadas sejam tratados como objetos da 
# classe base.


# Essa classe serve como a classe base comum para os animais e possui um método chamado
# "emitir_som()" vazio.
class Animal:  
    def emitir_som(self):  
        pass

# Definimos a classe derivada "Cachorro" que herda da classe base "Animal". Sobrescrevemos o 
# método "emitir_som()" para que ele imprima uma mensagem.
class Cachorro(Animal):  
    def emitir_som(self):  
        print("O cachorro está latindo: Au au!")

# Definimos a classe derivada "Gato" que também herda da classe base "Animal". Sobrescrevemos o 
# método "emitir_som()" para que ele imprima uma mensagem.
class Gato(Animal):  
    def emitir_som(self):
        print("O gato está miando: Miau!")

# Aqui, criamos objetos das classes derivadas e os atribuímos às variáveis respectivamente. 
# Esses objetos são instâncias das classes derivadas e herdam os métodos e atributos da classe 
# base "Animal".
cachorro = Cachorro()
gato = Gato()

# Aqui, chamamos o método "emitir_som()" em cada objeto. Como o polimorfismo está em ação, 
# mesmo que os objetos sejam tratados como objetos da classe base "Animal", a implementação 
# específica do método na classe derivada correspondente é executada.
cachorro.emitir_som() 
gato.emitir_som()     
