n = int(input('Digite um número para saber sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, n * c))
print('Fim')