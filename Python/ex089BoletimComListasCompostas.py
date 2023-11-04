geral = list()
while True:
    geral.append(list())
    geral[-1].append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    geral[-1].append(n1)
    n2 = float(input('Nota 2: '))
    geral[-1].append(n2)
    geral[-1].append(list())
    geral[-1][3].append((n1 + n2) / 2)
    esc = str(input('Quer continuar? [S/N] ').upper())
    if esc == 'N':
        break
print(geral)
print('-=' * 30)
print('No. NOME', end='')
print(' ' * 8, end=' ')
print('MÉDIA')
print('-' * 25)
for c, a in enumerate(geral):
    print(c, end='')
    print(' ' * 3, end='')
    print(geral[c][0], end='')
    esp = 13 - len(geral[c][0])
    print(' ' * esp, end='')
    print(geral[c][3])
print('-' * 25)
while True:
    esc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        break
    print(f'Notas de {geral[esc][0]}: \nN1: {geral[esc][1]}\nN2: {geral[esc][2]}')
