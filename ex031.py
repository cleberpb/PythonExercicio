'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de
até 200km, e R$ 0,40 para viagens mais longas.
'''

distancia = int(input('Digite o quilômetro da sua viagem: '))
perto = distancia * 0.50
longe = distancia * 0.40

if distancia <= 200:
    print('Sua viagem terá {}km de distância. Valor a pagar será de R${:.2f}.'.format(distancia, perto))
else:
    print('Sua viagem terá {}km de distância. Valor a pagar será de R${:.2f}.'.format(distancia, longe))
