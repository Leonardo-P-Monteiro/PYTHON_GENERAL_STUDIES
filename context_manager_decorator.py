# TRABALHANDO COM CONTEXT MANAGERS - ATRAVÉS DE UM DECORADOR E UMA GENERATION.
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening/creating the file.')
        file = open(file_path, mode)
        yield file
    
    except Exception as e:
        print('Ocorreu um erro: ', e)

    finally:
        print('Closing the file.')
        file.close()



instance_ = my_open('file_exemple_context_maneger_decorator_generation.txt', 'w')

with instance_ as file:
    file.write('Line 1\n',)
    file.write("I'm practice the context manager knowledge with the generator and decorator.\n")
    file.write('Line 3\n', 1235) # A excessão está aqui. Remova ela para o código roda inteiro.
