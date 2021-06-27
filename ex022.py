# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúculas.
# O nome com letras minúsculas.
# Quantas letras ao total, sem contar com os espaços.
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()  #strip elimina os espaços antes e depois.
print('Tudo em maiúsculo: {}.'.format(nome.upper()))
print('Tudo em minúsculo: {}.'.format(nome.lower()))
print('Quantas letra ao total: {}.'.format(len(nome) - nome.count(' ')))  # tamanho (len), menos (-) os espaços (count)
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
