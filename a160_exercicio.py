import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumentando os peços em 10%.
product_updating_prices = [
    {'nome':product['nome'], 'preco':round(product['preco'] * 1.10, 2)}
    for product in produtos
]

# Gerando uma nova lista de produtos sem relação com a lista original (Cópia profunda).
products_updated = copy.deepcopy(product_updating_prices)

# Ordenando os produtos: Ordem decrescente e cópia profunda (deep copy).
products_descender_order_name = sorted(copy.deepcopy(products_updated), key = lambda produto: produto['nome'], reverse=True)

# Ordene os produtos: Ordem crescente dos preços. Inseri cópia profunda por opção minha. 
products_growing_order_price = sorted(
    copy.deepcopy(products_updated),
    key= lambda p: p['preco'],
)
print('Lista original de produtos.')
print(*produtos, sep='\n')
print()
print('Lista de produtos com preço atualizado em 10%')
print(*products_updated, sep='\n')
print()
print('Lista de produtos ordenada por nome decrescente')
print(*products_descender_order_name, sep='\n')
print()
print('Lista de produtos ordenada por preço crescente')
print(*products_growing_order_price, sep='\n')

