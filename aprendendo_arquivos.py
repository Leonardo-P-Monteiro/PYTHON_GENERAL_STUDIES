arquivo_teste = 'arquivo_teste.txt' #

with open(arquivo_teste, 'w') as arquivo:
    arquivo.write('Oi! Estamos escrevendo no arquivo.\n')
    arquivo.write('Essa é uma linha de teste sequêncial.\n')
    arquivo.write('Se você está vendo essa mensagem estou exibido em comando.')

with open(arquivo_teste, 'r') as arquivo:
    print(arquivo.read())

    # Lista de strings para escrever no arquivo
linhas = ["Primeira linha.\n", "Segunda linha.\n", "Terceira linha.\n"]

# Abre o arquivo em modo de escrita ("w" para escrever)
with open("exemplo.txt", "w") as arquivo:
    arquivo.writelines(linhas)