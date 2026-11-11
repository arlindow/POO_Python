class Personagem:
    def __init__(self, nome, vida, poder):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        
    def atacar(self):
        print(self.nome, "atacou o inimigo!")
        
    def apresentar(self):
        print("Nome", self.nome)
        print("Vida", self.vida)
        print("Poder", self.poder)
        
class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome} lançou uma bola de fogo explosiva com {self.poder} de magia!")
    
class Arqueiro(Personagem):
    def atacar(self):
        print(f"{self.nome} disparou uma flecha certeira à distância com {self.poder} de impacto!")
        
class Ninja(Personagem):
    def atacar(self):
        print(f"{self.nome} lançou uma shuriken (estrela ninja) com {self.poder} de precisão!")
        
        
personagem1 = Personagem("Guerreiro", 100, 50)
personagem2 = Personagem("Mago", 80, 90)

mago = Mago("Mago", 100,100)
arqueiro = Arqueiro("Arqueiro", 200, 200)
ninja = Ninja("Shinobi", 300,300)




personagem1.apresentar()
personagem1.atacar()

personagem2.apresentar()
personagem2.atacar()

mago.atacar()
arqueiro.atacar()
ninja.atacar()
