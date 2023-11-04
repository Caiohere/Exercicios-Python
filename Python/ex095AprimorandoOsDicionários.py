grupo = []
jogador = {}
gp = []
while True:
    print('-=' * 35)
    jogador["nome"] = str(input('Nome do jogador: '))
    np = int(input('Quantas partidas {} jogou? '.format(jogador["nome"])))
    for c in range(0, np):
        gp.append(int(input('Quantos gols na {}º partida? '.format(c + 1))))
    jogador["gols"] = gp.copy()
    jogador["total"] = sum(gp)
    grupo.append(jogador.copy())
    jogador.clear()
    gp.clear()
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        break
print(f'{"No.":<4}{"nome":<10}{"gols":<10}{"total":10}')
print('-' * 33)
for i, v in enumerate(grupo):
    print('{}    {}      {}         {}'.format(i, v["nome"], v["gols"], v["total"]))
while True:
    esc = int(input('Mostrar dados de qual jogador? (999 para)'))
    if esc == 999:
        break
    for i, v in enumerate(grupo[esc]["gols"]):
        print('  Na partida {}, {} fez {} gols.'.format(i + 1,grupo[esc]["nome"], v))
    print('Foi um total de {} gols.'.format(grupo[esc]["total"]))
    print('-=' * 35)
