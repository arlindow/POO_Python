class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # Getter: metodo seguro para consultar o saldo(encapsulamento)
    def get_saldo(self):
        return self.__saldo
    
    # Setter: metodo com validacao antes de alterar o saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado.")
        else: 
            print("Valor invalido para deposito")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Saldo insuficiente ou invalido")

    # testando 

conta1 = ContaBancaria("Arlindo", 500)

conta1.depositar(200)
conta1.sacar(200)
# Tentativa de acesso direto a atributo privado:
print(f"Saldo Atual {conta1.get_saldo()}")
# -> Gera AttributeError: 'ContaBancaria' object has no attribute '__saldo'
print(conta1.__saldo)  
