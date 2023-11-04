import random
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 2° aluno: '))
n4 = str(input('Digite o nome do 3° aluno: '))
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print('A sequencia das apresentações será {}'.format(ordem))
