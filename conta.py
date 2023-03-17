
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Criando conta em disc ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    @property
    def extrato(self):
        print('Saldo {} na conta de titular {}'.format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor do saque ultrapassa o limite de {}".format(self.__limite))

    def transfere(self, valor, destino):
        if(valor <= self.__saldo):
            self.saque(valor)
            destino.deposito(valor)
            print("Feita transferencia no valor de {}".format(valor))
        else:
            print("O valor {} é maior que seu saldo atual {}".format(valor, sel.__saldo))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

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
    def codigo_banco():
        return "001"