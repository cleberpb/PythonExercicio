'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condições de pagamentos:
- Á vista dinheiro/cheque: 10% de desconto.
- Á vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''

valor_compra = float(input('Valor do Produto: '))
print('''
----------------------------------------------- 
|            OPÇÕES DE PAGAMENTO              |
| --------------------------------------------|
| 1 - Á vista no dinheiro/cheque: 10% desconto|
| 2 - Á vista no cartão: 5% de desconto.      |
| 3 - Em até 2x no cartão: preço normal.      |
| 4 - Em 3x ou mais no cartão: 20% de juros.  |
-----------------------------------------------''')
opcao = int(input('Escolha opção de pagamento: '))
dineiro_cheque = valor_compra - (valor_compra * 10 / 100)
cartao_2x = valor_compra - (valor_compra * 5 / 100)
cartao_3x_mais = valor_compra + (valor_compra * 20 / 100)

if opcao == 1:
    print('O Valor da compra é de R${:.2f}.'.format(valor_compra))
    print('Á vista no dinheiro/cheque, você tem 10% desconto. Valor a pagar R${}.'.format(dineiro_cheque))

elif opcao == 2:
    print('O Valor da compra é de R${:.2f}.'.format(valor_compra))
    print('Á vista no cartão, você terá 5% de desconto. Valor apagar é R${}.'.format(cartao_2x))

elif opcao == 3:
    print('O Valor da compra é de R${:.2f}.'.format(valor_compra))
    print('Em até 2x no cartão, você paga o preço normal.')

elif opcao ==4:
    print('O Valor da compra é de R${:.2f}.'.format(valor_compra))
    print('Em 3x ou mais no cartão, você terá 20% de juros. Valor apagar é R${}.'.format(cartao_3x_mais))

else:
    print('Escolha uma opção válida.')