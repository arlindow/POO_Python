class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        
    def acelerar(self):
        print("O carro está acelerando")
    
    def frear(self):
        print("O carro está freando") 
        

carro1 = Carro("Civic", "Preto")

print(carro1.modelo)
carro1.acelerar()
carro1.frear()


