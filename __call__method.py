# Esse dundermethod faz com que a instância da classe seja executável (ao utilizar os ())
class CallMe:
    def __init__(self, number):
        self.number = number
    
    def __call__(self, name):
        print(f'{name} está discando esse número {self.number}.')
        return 1234


call_1 = CallMe(85999068226)
return_ = call_1('Leo')
print(return_) # Exibindo o retorno do método __call__.
