# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele,
# usando as funções is.

n = input('Digite algo: ')
print('O seu tipo é', type(n))
print('É numerico? ', n.isnumeric())
print('É alfanumérico? ', n.isalnum())
print('É letra (as)? ', n.isalpha())
print('Só tem espaço? ', n.isspace())

