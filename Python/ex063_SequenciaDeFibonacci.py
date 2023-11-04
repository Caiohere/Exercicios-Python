c = 1
n = 0
n1 = 1
n2 = 1
nx = 0
n = int(input('Digite um número: '))
print('Sequencia de fibonacci {}x: '.format(n), end='')
print('1', end=' - ')
while c != n:
    if c == 1:
        print(n1, end=' - ')
    else:
        nx = n1 + n2
        print(nx, end=' - ')
    if c % 2 == 0:
        nx = n2 + n1
        n1 = nx
    else:
        nx = n1 + n2
        n2 = nx
    c += 1
print('Fim', end='')