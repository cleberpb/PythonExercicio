'''
Faça um programa que leia o peso de cisco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < peso:
            menor = peso
print(f'O maior peso lido foi {maior_peso}kg.')
print(f'O menor peso lido foi {menor_peso}kg.')
