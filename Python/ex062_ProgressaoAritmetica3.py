pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 1
esc = ''
cont = 0
term = 11
while c != term:
    if c == 1:
        print(pt, end=' - ')
    else:
        pt = pt + r
        print('{}'.format(pt), end=' - ')
    c = c + 1
    if c == term:
        esc = str(input('\nQuer continuar? \n[S/N]: ').upper())
        if esc == 'S':
            cont = int(input('Quantos termos deseja adicionar á PA? '))
            term += cont
        else:
            print('FIM')
