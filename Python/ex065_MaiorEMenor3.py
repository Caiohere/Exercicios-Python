c = 0
sn = 'S'
n = 0
alln = []
soma = 0
media = 0
while sn == 'S':
    n = int(input('Digite um número: '))
    c += 1
    alln.append(n)
    sn = str(input('Quer continuar? [S/N] ').upper())
print('O maior número: {}'.format(max(alln)))
print('O menor número: {}'.format(min(alln)))
soma = sum(alln)
print('A média é de: {}'.format(soma / c))

