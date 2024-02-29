from time import sleep
# VALIDANDO O PRIMEIRO DÍGITO #
print('Bem vindo ao validador de CPF!\U0001f9ee É preciso pontuar que esse é um script experimental com finalidade didática. Agradeço sua disponibilidade em conferir meu trabalho!\U0001f601  Fique a vontade para me enviar dicas ou apontar correções que sejam necessárias ao código.\U0001f4e7 \n')

# INSERINDO O Nº DO CPF E CONFIRMANDO SEUS DÍGITOS
while True:
    print('\n \u2328\uFE0F  ', end='')
    cpf_digitos = input('Insira o nº do CPF apenas dígitos: ').strip().replace('.', '').replace('-','')

# VALIDANDO TAMANHO E SE SÃO APENAS DÍGITOS.
    validar_digito = cpf_digitos.isdigit()
    if validar_digito == False:
        print('\n \u26A0\uFE0F	 ', end='')
        print('Por favor, digite apenas os números do CPF.')
        continue
    if len(cpf_digitos) != 11:
        print('\n \u26A0\uFE0F	 ', end='')
        print('CPF diferente de 11 dígitos. Tente novamente.')
        continue

# MULTIPLICANDO OS VALORES E OBTENDO RESULTADO.
    soma_digitos = 0
    multiplicador = 10
    for digito in cpf_digitos:
        if multiplicador >= 2:
            soma_digitos += int(digito) * multiplicador
            multiplicador = multiplicador - 1

# OBTENDO O VALOR DO PRIMEIRO DIGITO VERIFICADOR E CONFERINDO SE ELE É VÁLIDO.
    multiplicada_soma_digitos = soma_digitos * 10
    divisao_soma_digitos = multiplicada_soma_digitos % 11
    digito_verificador_1 = divisao_soma_digitos if divisao_soma_digitos <= 9 else 0
    if digito_verificador_1 != int(cpf_digitos[9]):
        print('\n \u26A0\uFE0F	 ', end='')
        print('CPF inválido. Motivo: Não passou no teste de autenticidade.')
        continue

# VALIDANDO O SEGUNDO DÍGITO #

    soma_digitos = 0
    multiplicador = 11
    for digito in cpf_digitos:
        if multiplicador >= 2:
            soma_digitos += int(digito) * multiplicador
            multiplicador = multiplicador - 1

    # OBTENDO O VALOR DO SEGUNDO DIGITO VERIFICADOR E CONFERINDO SE ELE É VÁLIDO.
    multiplicada_soma_digitos = soma_digitos * 10
    divisao_soma_digitos = multiplicada_soma_digitos % 11
    digito_verificador_2 = divisao_soma_digitos if divisao_soma_digitos <= 9 else 0
    if digito_verificador_2 != int(cpf_digitos[10]):
        print('\n \u26A0\uFE0F	 ', end='')
        print('CPF inválido. Motivo: Não passou no teste de autenticidade.')
        continue
    print('\n \u2714\uFE0F  ', end='')
    print('CPF válido. \n')
    print('\u26A0\uFE0F  ', end='')
    resp_continuar = input('Deseja continuar? [S]im ou [N]ão? ')
    resp_continuar = resp_continuar.lower()
    if resp_continuar == 's':
        continue
    else:
        print('\n \U0001f973  ', end='')
        print('Obrigado por utiliazar meu script! ')
        print('\n \u2714\uFE0F  ', end='')
        print('Programa finalizado. \n')
        sleep(15)
        break
    
