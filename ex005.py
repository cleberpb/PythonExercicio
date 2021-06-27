# Faça um programa que leia um número Inteiro
# e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
ant = numero - 1
suc = numero + 1
print('O número que você digitou foi {}.'.format(numero))
print('O seu antecessor é {}, e o seu sucessor é {}.'.format(ant, suc))
