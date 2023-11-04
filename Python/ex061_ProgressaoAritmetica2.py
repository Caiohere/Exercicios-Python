pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 1
while c != 11:
    if c == 1:
        print(pt, end=' - ')
    else:
        pt = pt + r
        print('{}'.format(pt), end=' - ')
    c = c + 1
print('FIM')
