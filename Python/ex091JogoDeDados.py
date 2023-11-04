from random import randint
from operator import itemgetter
from time import sleep
cont = 0
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    print('  O {} tirou {}'.format(k, v))
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, j in enumerate(ranking):
    print('  {}º lugar foi {} com {} pontos'.format(i + 1, j[0], j[1]))



