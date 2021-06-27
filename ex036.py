print('-=-'*14)
print('EMPRÉSTIMO PARA SUA CASA')
print('-=-'*14)

valor_casa = float(input('\nCasa no valor de qunato: '))
salario = float(input('Qual é o seu salário: '))
anos_pagamento = int(input('Quantos anos para pagar: '))

porcentagem = salario * 30 / 100
prestacao = valor_casa / (12 * anos_pagamento)


if prestacao <= porcentagem:
    print('\n*******************************************')
    print('* PARABÉNS! O seu empréstimo foi APROVADO!*')
    print('*******************************************')
    print('O valor da Prestação será de R$ {:.2f}.'.format(prestacao))
else:
    print('Empréstino NÃO APROVADO.')
