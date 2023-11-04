def fatorial(n, show=False):
    """
     Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    i = soma = n
    for c in range(i-1, 0, -1):
        soma = soma * c
    if show:
        print(f'{n} x ', end='')
        for c in range(i - 1, 0, -1):
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
    return soma


print(fatorial(5, show=True))
#help(fatorial)
