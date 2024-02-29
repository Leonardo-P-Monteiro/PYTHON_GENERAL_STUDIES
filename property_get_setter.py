class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        print('Estou no setter.')
        if valor < 0:
            raise ValueError("A idade não pode ser negativa")
        self._idade = valor
        print(self._idade)

# Exemplo de uso
pessoa = Pessoa("João", 30)
print(pessoa.nome)  # Acesso ao atributo 'nome'
print(pessoa.idade)  # Acesso ao atributo 'idade'

pessoa.idade = 35  # Modificação do atributo 'idade'
print(pessoa.idade)  # Acesso ao atributo 'idade'

# Tentativa de definir idade como valor negativo
try:
    pessoa.idade = -5
except ValueError as e:
    print(str(e))