# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

tempo = float(input('Informe a temperatura em Cº: '))
fahrenheit = ((tempo * 9) / 5) + 32  # formula para converter Cº em Fº.
print('A temperatura informada em Cº é {}, mas em Fº é {}.'.format(tempo, fahrenheit))
