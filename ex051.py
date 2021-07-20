'''
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA(Progressão Aritmética). No final,
mostre os 10 primeiros termos desta progressão.
'''

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for conta in range(primeiro_termo, decimo + razao, razao):
    print(f'{conta}', end='  → ')
print('ACABOU!!')

'''
Outro exemplo, digitando o 1º termo, 2º termo e a razão.

primeiro_termo = int(input('Digite o pimeiro termo: '))
segundo_termo = int(input('Digite o segunto termo: '))
razao_pa = int(input('Digite a razão: '))

for progressao in range(primeiro_termo, segundo_termo+1, razao_pa)[0:10]:
    print(progressao, end=' -> ')
print('ACABOU!\n')
'''
