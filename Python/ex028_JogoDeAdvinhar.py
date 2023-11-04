import random
print('Jogo da advinha! O computador escolherá um n° de 1 á 5.')
n1 = random.randint(1, 5)
jogo = int(input('tente advinhar qual número o computador escolheu: '))
if jogo == n1:
    print('Você acertou!')
else:
    print('Você errou!')
print('Fim')