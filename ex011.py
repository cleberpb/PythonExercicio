# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura da parede: '))
altura = float(input("Digite a altura da parede: "))
soma = largura * altura
tinta = soma / 2
print('Com um litro de tinta, você pinta 2m² de parede.')
print('Sua parede tem {:.2f} metros de largura e {:.2f} metros de altura.'.format(largura, altura))
print('Para {:.2f} metros de parede, você precisará de {:.2f} de tinta.'.format(soma, tinta))
