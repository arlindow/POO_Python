class Animal:
    def __init__(self,nome, idade,som):
        
        self.nome = nome
        self.idade = idade 
        self.som = som
        
    def emitir_som(self):
        print(f"O {self.nome} está {self.som}")
        
        
class Cachorro(Animal):
    pass
    
class Gato(Animal):
    pass
    
    
dog1 = Cachorro("Dog", 5, "latindo: au au")
gato1 = Gato("Gato", 4, "miando: miaaauuuuu" )
dog2 = Animal("Neno", 1, "choromingando")



dog1.emitir_som()
gato1.emitir_som() 
dog2.emitir_som()
       