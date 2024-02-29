import locale

# Define a localidade para o formato brasileiro (pt_BR)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Valor monetário que você deseja formatar
valor = 12345.67

# Usa a função locale.currency para formatar o valor de acordo com a localidade
# definida
valor_formatado = locale.currency(valor, grouping=True, symbol=True)

# Exibe o valor formatado
print(f"Valor formatado: {valor_formatado}")