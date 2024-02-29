# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y
    


def multiplica(x, y):
    return x * y 
    


def criar_funcao(funcao, x):
    def function_intern (y):
        return funcao(x, y)
    return function_intern


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

# OPERANDO TESTES
print(soma_com_cinco(1)) # OK
print(multiplica_por_dez(2)) # OK