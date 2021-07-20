'''
Refaça o Desafio ex09, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um
laço for.
'''

print('-='*18)
print('TABUADA')
print('-='*18)
numero = int(input('Digite um número para a tabuada: '))
print(f'Segue abaixo a tabuada de {numero}.\n')
for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f'{numero} x {tabuada} = {resultado}')
print('\n')