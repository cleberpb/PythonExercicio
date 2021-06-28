'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km/h acima do limete.
'''

print('Velocidade acima de 80km/h será multado. A multa será de R$ 7,00 por cada km.')
velocidade = int(input('Digite a velocidade de um veículo: '))
multa = velocidade % 80 * 7.00

if velocidade <= 80:
    print('Tenha uma ótima viagem.')
else:
    print(f'ATENÇÃO! Sua velocidade foi de {velocidade} km/h.')
    print('Você foi multado em R${:.2f}.'.format(multa))
print('Dirija com cuidade.')
