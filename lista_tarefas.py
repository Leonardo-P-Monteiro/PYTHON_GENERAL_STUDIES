import os

def adicionar(tarefa, lista_tarefas):
    tarefa = input('Digite a tarefa: ').strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    lista_tarefas.append(tarefa)
    salvar([tarefa], CAMINHO_ARQUIVO)
    return


def remover(lista_tarefas):
    tarefa_removida = lista_tarefas.pop()
    tarefas_removidas.append(tarefa_removida)
    print(f'Tarefa: {tarefa_removida} foi removida da lista.')
    print()
    sobrescrever(lista_tarefas, CAMINHO_ARQUIVO)
    return


def listar(lista_tarefas):
    if not lista_tarefas:
        print('Lista vazia. Não há tarefas.')
        return
    print('Lista de tarefas:')
    for tarefa in lista_tarefas:
        print(f' - {tarefa}')
    print()
    return


def desfazer(tarefas_removidas):
    if not tarefas_removidas:
        print('Não há histórico de tarefas removidas.')
        return
    tarefa_removida = tarefas_removidas.pop()
    lista_tarefas.append(tarefa_removida)
    print(f'A tarefa "{tarefa_removida}" foi reescrita.')
    sobrescrever(lista_tarefas, CAMINHO_ARQUIVO)
    print()
    return


def limpar_tela():
    os.system('cls')

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'a') as arquivo:
        for tarefa in tarefas:
            str(tarefa)
        dados = arquivo.writelines(f'{tarefa} \n')
    return dados 


def sobrescrever(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        for tarefa in tarefas:
            str(tarefa)
        dados = arquivo.writelines(f'{tarefa} \n')
    return dados 


CAMINHO_ARQUIVO = 'lista_tarefas.txt'
lista_tarefas = []
tarefas_removidas = []

print('Lista de tarefas')
while True:
    
    print('Comandos: adicionar, remover, listar, desfazer, limpar tela.')
    tarefa = input('Digite um comando: ').strip()
    print()
    
    if tarefa == 'adicionar':
        adicionar(tarefa, lista_tarefas)
        continue
    elif tarefa == 'remover':
        remover(lista_tarefas)
        continue
    elif tarefa == 'listar':
        listar(lista_tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas_removidas)
        continue
    elif tarefa == 'limpar tela':
        limpar_tela()
        continue
    else:
        print('Comando inválido. Digite um comando válido.')
    