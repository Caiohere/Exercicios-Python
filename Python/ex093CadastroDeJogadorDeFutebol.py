jogador = {}
gp = []
jogador["nome"] = str(input('Nome do jogador: '))
np = int(input('Quantas pastidas {} jogou? '.format(jogador["nome"])))
for c in range(0, np):
    gp.append(int(input('Quantos gols na {}º partida? '.format(c + 1))))
jogador["gols"] = gp
jogador["total"] = sum(gp)
print('-=' * 35)
print(jogador)
print('-=' * 35)
print('O jogador {} jogou {} partidas'.format(jogador["nome"], np))
for i, v in enumerate(jogador["gols"]):
    print('  Na partida {}, fez {} gols.'.format(i + 1, v))
print('Foi um total de {} gols.'.format(jogador["total"]))
print('-=' * 35)
