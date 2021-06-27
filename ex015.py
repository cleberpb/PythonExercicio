# Escreva um programa que pergunte a quantidade de Km percorridos
#  por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos quilometros foi percorrido? '))
valor_carro = 60.00
km_rodado = 0.15
total = valor_carro * dias + km * km_rodado

print('O valor do aluguel do carro ao dia é R${}, mas R${} centavos por km rodado.'.format(valor_carro, km_rodado))
print('O valor total a pagar é R${}.'.format(total))
