'''
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se eles podem ou não formar um triângulo.
'''


print('-=-'*15)
print('Analizador de um Triângulo')
print('-=-'*15)
primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo!')
