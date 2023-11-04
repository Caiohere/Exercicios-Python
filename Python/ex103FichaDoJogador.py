def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato.')


nome = str(input('Qual o nome do jogador: '))
gols = str(input(f'Quantos gols {nome} fez?: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(jogador=nome, gols=gols)

