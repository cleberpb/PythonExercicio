'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o
valor for ímpar, desconsidere-o.
'''

soma = 0
contador = 0
for repete in range(1, 7):
    numero = int(input(f'Digite o {repete}º valor: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'Você digitou {contador} números PARES e a soma deles foi {soma}.')
