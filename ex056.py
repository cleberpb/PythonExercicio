'''
Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

media = 0
menor = 0
mulher = 0

for pessoas in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Qual é sua idade: '))
    sexo = str(input('Sexo: Homem/Mulher: ')).lower()
    print('\n')

    media = media + idade
    if sexo == mulher:
        sexo = mulher
    if mulher <= 19 :
        mulher = menor + 1

print(f'A média de idade do grupo de pessoas é de {media / 4}')
print(f'{mulher} mulheres tem menos de 20 anos.')
