class Escritor:
    def __init__(self, nome):
        self._nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaEscrever:
    def __init__(self, nome):
        self._nome = nome
    
    def escrevendo(self):
        return f'{self._nome} está escrevendo...'
    
escritor_leonardo = Escritor('Leonardo')
teclado = FerramentaEscrever('Teclado')
escritor_leonardo.ferramenta = teclado
print(escritor_leonardo.ferramenta.escrevendo())
print(escritor_leonardo.ferramenta._nome)