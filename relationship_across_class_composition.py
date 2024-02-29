class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._endereco = []

    def inserir_endereco(self, rua, numero):
        self._endereco.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self._endereco:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente_1 = Cliente('Leonardo')
cliente_1.inserir_endereco('Rua João Domingos de Paiva', 170)
cliente_1.inserir_endereco('Av. Visconde do Rio Branco', 2274)
print(cliente_1._nome)
cliente_1.listar_endereco()