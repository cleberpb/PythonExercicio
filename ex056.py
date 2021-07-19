'''
Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

media_idade = 0
mais_velho = 0
menoridade = 0

for pessoas in range(1, 5):
    nome = input('Qual é o seu nome? ')
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Sexo: M ou F? ')
    media_idade = media_idade + idade
    
print(media_idade / 4)


