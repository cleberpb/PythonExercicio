# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
separacao = nome.split()
print('O seu primeira nome é {}.'.format(separacao[0]))
print('E o último é {}.'.format(separacao[-1]))  # [-1] começa do final para o inicio da lista.
