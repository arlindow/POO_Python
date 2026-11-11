class Carro:
    def __init__(self, marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def apresentar(self):
        print("Marca", self.marca)
        print("Modelo", self.modelo)
        print("Ano", self.ano)
        
    def acelerar(self):
        print(self.modelo, "Está acelerando!")

carro1 = Carro("Toyota", "Corolla", 2024)
carro2 = Carro("Honda", "Civic", 2023)
carro3 = Carro("Volkswagen", "Gol", 2020)
carro4 = Carro("Fiat", "Mobi", 2022)

carro1.apresentar()
carro1.acelerar()

