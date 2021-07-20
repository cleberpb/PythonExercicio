'''
Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_do_velho = ''
total_mulher20 = 0

for pessoa in range(1, 5):
    print(f'-------- {pessoa}ª PESSOA --------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [ M/F ]: ')).strip()
    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_do_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1
media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade}.')
print(f'O homem mais velho tem {maior_idade_homem} idade e se chama {nome_do_velho}.')
print(f'Ao todos são {total_mulher20} mulher(es) com menos de 20 anos.')
