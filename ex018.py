# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor do Ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Você digitou o ângulo {}.'.format(angulo))
print('Seu seno é {:.4f}, o cosseno {:.4f} e a tangente {:.4f}.'.format(seno, cosseno, tangente))
