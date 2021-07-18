# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua  média.

nota1 = float(input('Digite a primeira nota do aluno(a): '))
nota2 = float(input('Digite a segunda nota do aluno(a): '))
media = (nota1 + nota2) / 2
print('Você tirou as nostas {} e {}, a sua média é {:.2f}'.format(nota1, nota2, media))
