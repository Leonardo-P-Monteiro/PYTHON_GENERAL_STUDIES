from time import sleep


# LISTA DE PERGUNTAS OK
perguntas = [
    {'Pergunta': 'Para qual tipo de relacionamento comercial é mais indicada a cold call?',
     'Opções': ['B2C', 'C2B', 'B2B', 'C2C',],
     'Resposta': 'B2B'
    },
    {'Pergunta': 'Qual foi a teoria criada por Frederick Taylor?',
     'Opções': ['Teoria Científica da Administração', 'Teoria Clássica da Administração', 'Teoria da Contingência', 'Teoria Neoclássica'],
     'Resposta': 'Teoria Científica da Administração'
    },
    {'Pergunta': 'É a principal peça contábil, que fornece uma visão global do negócio em um dado momento.',
     'Opções': ['Balanço Patrimonial', 'Nota Fiscal', 'DFC', 'IRPJ'],
     'Resposta': 'Balanço Patrimonial'
    },
]
contador_correta = 0
contador_errada = 0
# CHAMADAS DA PERGUNTA 1
print('❓ Pergunta: ', perguntas[0]['Pergunta'], '\n')
print('📝 Opções: \n')
for indice, valor in enumerate(perguntas[0]['Opções']):
    print(indice, ') ', valor)
resposta_0 = int(input('Informe uma das opções: '))
resposta_0_c = perguntas[0]['Resposta']
if perguntas[0]['Opções'][resposta_0] == resposta_0_c:
    print('Resposta correta! 👏 \n')
    contador_correta += 1
else:
    print('Resposta errada. 😔 \n')
    contador_errada += 1
sleep(1.2)
print('\n')
# CHAMADAS DA PERGUNTA 2
print('❓ Pergunta: ', perguntas[1]['Pergunta'], '\n')
print('📝 Opções: \n')
for indice, valor in enumerate(perguntas[1]['Opções']):
    print(indice, ') ', valor)
resposta_1 = int(input('Informe uma das opções: '))
resposta_1_c = perguntas[1]['Resposta']
if perguntas[1]['Opções'][resposta_1] == resposta_1_c:
    print('Resposta correta! 👏 \n')
    contador_correta += 1
else:
    print('Resposta errada. 😔 \n')
    contador_errada += 1
sleep(1.2)
# CHAMADAS DA PERGUNTA 3
print('❓ Pergunta: ', perguntas[2]['Pergunta'], '\n')
print('📝 Opções: \n')
for indice, valor in enumerate(perguntas[2]['Opções']):
    print(indice, ') ', valor)
resposta_2 = int(input('Informe uma das opções: '))
resposta_2_c = perguntas[2]['Resposta']
if perguntas[2]['Opções'][resposta_2] == resposta_2_c:
    print('Resposta correta! 👏 \n')
    contador_correta += 1
else:
    print('Resposta errada. 😔 \n')
    contador_errada += 1
sleep(1.2)
print(f'Respostas corretas: {contador_correta}','\n',f'Respostas erradas: {contador_errada}')
sleep(1)
print('Fim do formulário!')
sleep(10)