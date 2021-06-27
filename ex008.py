# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite uma metragem: '))
centimentro = metro * 100
milimetro = metro * 1000
print('Você digitou {:.2f} metros.'.format(metro))
print('Em centímetro dá {}.'.format(centimentro))
print('E em milímetro dá {}.'.format(milimetro))

