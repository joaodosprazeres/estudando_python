class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return valor < self.__saldo + self.__limite

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("saldo insuficiente")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_conta():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "154", "Bradesco": "237"}


from conta import Conta
conta = Conta(123, "Nico", 55.5, 1000.0)
conta.saca(10000)
conta.codigo_banco()