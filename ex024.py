# Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.

'''
Eu resolvi assim:
cidade = str(input('Digite o nome de uma cidade: ')).strip()
maiuscula = cidade.lower()
lista = maiuscula.split()
primeiro_nome = lista[0]
print('santo' in primeiro_nome)
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')  # as 5 primeiras letras são igual a SANTO, colocado para caixa alta.
