# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: '))
aumento = salario + (salario * 15 / 100)
print('Seu salário atual é R$ {:.2f}, mas com 15% de aumento, ficará R$ {:.2f}.'.format(salario, aumento))
