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

class Ave(Animal):
    def voar(self):
        print("voando")
    
    
dog1 = Cachorro("Dog", 5, "latindo: au au")
gato1 = Gato("Gato", 4, "miando: miaaauuuuu" )
dog2 = Animal("Neno", 1, "choromingando")
pardal1 = Ave("Phoenix", 4, "gritando... Arrghhh")
dog3 = Cachorro("Ralf", 6, "ainnn")

dog1.emitir_som()
gato1.emitir_som() 
dog2.emitir_som()
pardal1.emitir_som()
pardal1.voar() 
dog3.emitir_som()      