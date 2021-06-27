# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

valor_produto = float(input('Digite o valor do produto: '))
desconto = valor_produto - (valor_produto * 5 / 100)
print('O valor do produto é de R$ {:.2f}, mas com 5% de desconto, ficará R$ {:.2f}.'.format(valor_produto, desconto))
