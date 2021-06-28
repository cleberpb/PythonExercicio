'''
Desenvolva um lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.6 e 25: Peso ideal.
- 25.1 até 30: Sobrepeso.
- 30.1 até 40: Obesidade.
Acima de 40.1: Obsidade mórbida.
'''

print('Vamos saber o seu IMC - Índice de Massa Corpórea')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura**2)

if imc <= 18.5:
    print('Seu peso é {:.2f}kg, sua altura é {:.2f} m.'.format(peso, altura))
    print('Seu IMC é de {:.2f}. Você está abaixo do peso.'.format(imc))
elif imc >= 18.6 and imc <= 25:
    print('Seu peso é {:.2f}kg, sua altura é {:.2f} m.'.format(peso, altura))
    print('Seu IMC é de {:.2f}. Você está com o pesos ideal.'.format(imc))
elif imc >= 25.1 and imc <= 30:
    print('Seu peso é {:.2f}kg, sua altura é {:.2f} m.'.format(peso, altura))
    print('Seu IMC é de {:.2f}. Você com sobrepeso.'.format(imc))
elif imc >= 30.1 and imc <= 40:
    print('Seu peso é {:.2f}kg, sua altura é {:.2f} m.'.format(peso, altura))
    print('Seu IMC é de {:.2f}. Você está com obsidade.'.format(imc))
else:
    print('Seu peso é {:.2f}kg, sua altura é {:.2f} m.'.format(peso, altura))
    print('Seu IMC é de {:.2f}. Você está com obsidade mórbida.'.format(imc))
