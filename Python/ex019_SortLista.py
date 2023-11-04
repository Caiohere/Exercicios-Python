import random
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 2° aluno: '))
n4 = str(input('Digite o nome do 3° aluno: '))
aluno = random.choice([n1, n2, n3, n4])
print('O aluno escolhido para apagar a lousa foi o {}'.format(aluno))
