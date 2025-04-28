class Calculadora:

    def somar(self,a,b,c=None):
        if c is None:
            return a+b
        else:
            return a+b+c
    
    def subtrair(self,a,b,c=None):
        if c is None:
            return a-b
        else:
            return a-b-c

Brastempe = Calculadora()
print("Adicao: \n", Brastempe.somar(9, 10))
print(Brastempe.somar(102, -23, 5.1))

print("\nSubtracao:\n", Brastempe.subtrair(9, 10))
print(Brastempe.subtrair(102, -23, 5.1))
