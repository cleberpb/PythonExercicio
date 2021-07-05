'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o
valor for ímpar, desconsidere-o.
'''

total = 0
for somar in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        total = total + numero
print(f'Total dos números pares são {total}.')
