'''
Faça um programa que leia o peso de cisco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
maior_peso = 0
menor_peso = 0
for pessoa_peso in range(1, 6):
    peso = float(input('Qual é o seu peso? '))
    if peso < maior_peso:
        menor_peso = menor_peso + peso
    if peso > menor_peso:
       maior_peso = maior_peso + peso
print(f'O menor peso é {menor_peso}')
print(f'O maior peso é {maior_peso}')