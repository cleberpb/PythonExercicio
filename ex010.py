# Crie um programa que leia quantos dinheiro uma pessoa tem na carteira
# e mostre quantos dólares(valor atual) ela pode comprar.

dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
dolar = float(input('Digite a contação do dólar atual: '))

compra = dinheiro / dolar
print('Com R$ {:.2f}, você compra $ {:.2f} dolares.'.format(dinheiro, compra))
