n = 0
c = 0
n = int(input('Digite um número para saber sua tabuada: '))
while c != 10:
    if n < 0:
        break
    else:
        c += 1
        print('{}x{} = {}'.format(n, c, n * c))
        if c == 10:
            n = int(input('\nDigite outro número: '))
            c = 0
            if n < 0:
                break
print('Encerrado, até mais!')
