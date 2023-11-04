from random import randint
lista = list()
esc = int(input('quantos jogos você quer que eu sorteie? '))
for c in range(0, esc):
    lista.append(list())
for i in lista:
    for c in range(0, 6):
        n = randint(0, 60)
        if c == 0:
            i.append(n)
        else:
            if n not in i:
                i.append(n)
            else:
                n = randint(0, 60)
                i.append(n)
for c in range(0, esc):
    if c == 0:
        print(f'Jogo 1: {lista[0]}')
    else:
        print(f'Jogo {c + 1}: {lista[c]}')