salario = float(input('Qual é o salário do funcionário: R$ '))
menor_salario = salario + (salario * 15 / 100)
maior_salario = salario + (salario * 10 / 100)

if salario <= 1250:
    print('Quem ganhava R$ {:.2f} passar a ganhar R$ {:.2f}.'.format(salario, menor_salario))
else:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}.'.format(salario, maior_salario))
