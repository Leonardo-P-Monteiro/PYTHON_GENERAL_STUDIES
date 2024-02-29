# Classes decoradoras.
import __call__method


# AQUI O MÚLTIPLICADOR É DINÂMICO.
class SumMultiplier:
    """Oi! Essa é nossa docstring teste."""
    def __init__(self, multiplier):
        self.multiplier = multiplier
    

    def __call__(self, func):
        def intern_func(*arg, **kwarg):
            operation = func(*arg, **kwarg)
            return operation * self.multiplier
        return intern_func

    def exemple():
        pass




# AQUI FAZEMOS DE MANEIRA QUE O MULTIPLICADOR É ESTÁTICO.
# class SumMultiplier:
#     def __init__(self, func):
#         self.func = func
#         self.multiplier = 2 # Aqui estou definindo o multiplicador.
    
#     def __call__(self, *arg, **kwarg):
#         result_multiplier_sum = self.func(*arg, **kwarg)
#         return result_multiplier_sum * self.multiplier
    




@SumMultiplier(2) # Depois desses primeiros () existe implícitamente mais um par (). Pois é o do método __call__.
# @SumMultiplier
def sum(x, y):
    return x+y


sum_ = sum(1, 2)
print(sum_)
# print(SumMultiplier.__doc__)
help(__call__method)
# help(sum)
