pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
dec = pt + (10 - 1) * r
for c in range(pt, dec + 1, r):
    print('{}'.format(c), end=' - ')
print('Fim')