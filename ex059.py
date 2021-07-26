'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] qual o maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

numero1 = 0
numero2 = 0
opcao = 0
divisoria = '*'*33


while opcao != 5:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))

    print('''
    ---------------------
    | ESCOLHA UMA OPÇÃO |
    |-------------------|
    | [1] Somar         |
    | [2] Multiplicar   |
    | [3] Qual o maior  |
    | [4] Novos números |
    | [5] Sair          |
    ---------------------
    ''')
    opcao = int(input('Digite uma opção: '))


    if opcao == 1:
        soma = numero1 + numero2
        print(f'A soma de {numero1} + {numero2}={soma}.')
        print(divisoria, '\n')
    if opcao == 2:
        multiplcacao = numero1 * numero2
        print(f'A multiplicação de {numero1} x {numero2}={multiplcacao}')
        print(divisoria, '\n')
    if opcao == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que {numero2}.')
            print(divisoria, '\n')
        else:
            print(f'O número {numero2} é maior que {numero1}.')
            print(divisoria, '\n')
    if opcao == 4:
        print(divisoria, '\n')
    if opcao == 0 or opcao > 5:
        print('Opção inválida. Tente novamente.')
        print(divisoria, '\n')
print('Você saiu do programa')
