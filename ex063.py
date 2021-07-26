'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elemento de uma Sequência de Fibonacci.
Ex:
0 ⇾ 1 ⇾ 1 ⇾ 2 ⇾ 3 ⇾ 5 ⇾ 8
'''

numero = 0
elementos = 0
#soma = 0

while numero < elementos:
    numero = int(input('Digite um número: '))
    elementos = int(input('Digite quantos elementos da Seguência de Fibonacci: '))
    soma = numero + numero
    print(soma)
