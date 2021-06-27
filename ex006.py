# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)

print('Você digitou o número {}.'.format(n1))
print('O seu dobro é {}.'.format(dobro))
print('O seu triplo é {}, e sua raiz quadrada é {:.2f}.'.format(triplo, raiz))
