'''Faça um programa que calcula e soma entre todos os
números impares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.'''

soma = 0       # acumulador, soma os valores ou multiplica etc.
contador = 0   # contador conta mais 1, quando repete o laço, conta 1 + 1 = 2 etc.
for multiplos in range(1, 501, 2):
    if multiplos % 3 == 0:
        soma += multiplos
        contador += 1
print(f'\nA soma de todos os {contador} valores solicitados é de {soma}.\n')