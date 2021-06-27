# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))

sorteio = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado para apagar o quadro foi: {}'.format(sorteio))
