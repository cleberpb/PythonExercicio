'''
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferente.
'''


print('-=-'*15)
print('Analizador de um Triângulo')
print('-=-'*15)
primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
    if primeiro == segundo and primeiro == terceiro and segundo == terceiro:
        print('Esse triângulo tem todos os lados iguas, ele é Equilátero')
    elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
        print('Esse trinângulo tem todos os lados diferentes, ele é Escaleno')
    elif True:
        print('Esse triângulo tem dois lados iguais, ele é Isósceles')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo!')
