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
print(imc)

if imc <= 18.5:
    print('Seu peso é {:.2f}kg e seu IMC é {:.2f}. Você está abixo do peso.'.format(peso, imc))
elif imc >=18.6 and <=25:
    print('')
