from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim:
        print('-=' * 15)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for n in range(inicio, fim + 1, passo):
            print(f' {n}', end='')
            sleep(0.5)
        print()
        print('-=' * 15)
    else:
        print('-=' * 15)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for n in range(inicio, fim - 2, -passo):
            print(f' {n}', end='')
            sleep(0.5)
        print()
        print('-=' * 15)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
