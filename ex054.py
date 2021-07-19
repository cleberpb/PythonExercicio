'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
Considerando a maioridade 21 anos.
'''
menoridade = 0
maioridade = 0
for pessoas in range(1, 8):
    ano = int(input('Quantos anos você tem? '))
    if ano <= 20:
        menoridade = menoridade + 1
    if ano >= 21:
        maioridade = maioridade + 1
print(f'{menoridade} pessoa(as) tem menoridade.')
print(f'{maioridade} pessoa(as) tem maioridade.')

   

