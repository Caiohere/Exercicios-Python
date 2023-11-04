c = 0
n = 0
soma = 0
n = int(input('Digite um número para saber seu fatorial: '))
while c != n - 1:
    c = c + 1
    if c == 1:
        soma = 1 * n
    soma = soma * c
print('{}!= '.format(n),end='')
for a in range(1, n + 1):
    print('{}'.format(a), end='')
    print('x' if a < n else '= ', end='')
print(soma)