class Carrinho:
    def __init__(self):
        self._produtos = []
       
    def inserir_produto(self, produto):
        self._produtos.append(produto)

    def listar_produtos (self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
    
    def preco_total (self):
        return print(f' Preço total: {sum([p.preco for p in self._produtos])}')

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho_compras = Carrinho()
produto_1 = Produto('Caderno', 12)
carrinho_compras.inserir_produto(produto_1)
carrinho_compras.listar_produtos()
carrinho_compras.preco_total()
produto_2 = Produto('Lápis', 2.5)
carrinho_compras.inserir_produto(produto_2)
carrinho_compras.preco_total()
