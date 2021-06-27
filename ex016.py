# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.
# Ex: digite um número: 6.127 O número 6.127 tem a parte Inteira 6.
import math

numero = float(input('Digite um número Real (exemplo: 6.127):'))
print('O número que você digitou foi {}, o seu inteiro é {}.'.format(numero, math.trunc(numero)))
