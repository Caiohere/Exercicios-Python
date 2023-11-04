from time import sleep


def maior(num):
    cont = 0
    bigger = 0
    print('Analisando os valores informados...')
    sleep(1.5)
    while True:
        for c, n, in enumerate(num):
            if c == 0:
                bigger = num[c]
            else:
                if num[c] > bigger:
                    bigger = num[c]
        cont += 1
        if cont == len(num):
            break
    for c, n in enumerate(num):
        print(f'{n}', end=' ')
    print(f'Foram informados {len(num)} ao todo')
    print(f'O maior valor foi {bigger}')


print('=-' * 25)
valores = [4, 7, 0]
maior(valores)
