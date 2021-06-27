# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

cateto_o = float(input('Digite o valor de catete oposto: '))
cateto_a = float(input('Digite o valor de cateto adjacente: '))
hipotenusa = math.hypot(cateto_o, cateto_a)
print('O cateto oposto {} e a cateto adjacente {}, sua hipotenusa é {}.'.format(cateto_o, cateto_a, hipotenusa))
