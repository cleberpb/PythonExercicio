# Crie um script python que leia
# o nome de uma pessoa e mostre uma mensagem
# de boas-vindas de acordo com o valor digitado.

nome = input('Digite o seu nome: ')
# print('É um prazer te conhecer,', nome,) - Pde fazer desta forma.
print('É um prazer te conhecer, {}!'.format(nome))  # ou desta outra forma.
