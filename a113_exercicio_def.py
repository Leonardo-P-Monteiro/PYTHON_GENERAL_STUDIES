def multiplicador(*args):
    acumulador = 1
    for argumentos in args:
        acumulador *= argumentos
    return acumulador


def par_impar(n):
    teste = n % 2 == 0
    if teste:
        return f'{n} é par.'
    return f'{n} é ímpar.'
    #if n % 2 == 0:
    #    return 'Número é par'
    #else:
    #    return 'Número é ímpar'
    

operacao = multiplicador(3, 3)
print(operacao)
print(par_impar(operacao))