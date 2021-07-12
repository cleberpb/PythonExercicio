'''
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA(Progressão Aritmética). No final,
mostre os 10 primeiros termos desta progressão.
'''


primeiro_termo = int(input('Digite o pimeiro termo: '))
segundo_termo = int(input('Digite o segunto termo: '))
razao_pa = int(input('Digite a razão: '))

for progressao in range(primeiro_termo, segundo_termo, razao_pa):
    print(progressao)
print(f'O primeiro termo é {primeiro_termo}.')
print(f'O Segundo termo é {segundo_termo}.')
print(f'A razão é {razao_pa}.')
