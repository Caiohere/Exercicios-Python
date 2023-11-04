from random import randint
from time import sleep


def sorteio(lista):
    print('sorteando 5 valores da lista:', end=' ')
    for c in range(1, 6):
        n = randint(0, 60)
        print(f'{n}', end=' ')
        sleep(0.5)
        lista.append(n)
    print()


numeros = list()
sorteio(numeros)


def somapar(lista):
    print(f'Somando os valores pares de {lista},', end=' ')
    pares = 0
    for c, i in enumerate(lista):
        if i % 2 == 0:
            pares += i
    print(f'temos {pares}')


somapar(numeros)

