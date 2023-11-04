c = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        c += 1
    if n == 999:
        break
    cont = cont + n
print('A quantidade de número digitados: {}'.format(c))
print('A soma de todos os número digitados: {}'.format(cont))
