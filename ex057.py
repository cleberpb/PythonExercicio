'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errada, peça a condição
novamente até ter um valor correto.
'''


m = 'm'
f = 'f'
sexo = ''

while sexo != m and sexo != f:
    sexo = str(input('\nDigite o sexo [ M / F ]: ')).lower().strip()
    if sexo != m and sexo != f:
        print('O sexo deve ser M ou F. Digite novamente.')
    print('-='*21)
    
print(f'O sexo digitado foi {sexo.upper()}.\n')

'''
Codigo de professor

sexo = str(input('Informe o sexo: [M / F]: ')).strip().upper()
while sexo not in 'MmFf': # enquanto 'MNFf' não estiver em sexo. Estou lendo assim para o entendimento.
    sexo = str(input('Opção inválida. Escolher M ou F: ')).strip().upper()[0] 
print(f'Sexo {sexo} registrado com sucesso.')

OBS:
- O fatiamento [0]aceita varias palavras começando com m e f.
- O valor em branco, está passando pela validação.
'''