class conta_banc:
    def __init__(self, saldo_inic):
        self._saldo = saldo_inic

    def depositar(self,valor):
        if valor>0:
            self._saldo+=valor
            print(f'deposito de {valor} realizado.\nSaldo atual: {self._saldo}')
        else:
            print('Valor de deposito inválido.')

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de {valor} realizado.\nSaldo atual: {self._saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido")

    def get_saldo(self):
        return self._saldo
    
    def Biplio.depositar(self._saldo, {valor}):
        

valor_deposito = input(str('Digite o valor que deseja depositar: '))
print(Biplio.depositar('valor_deposito'))
