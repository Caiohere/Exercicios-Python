peso = 0
maior = 0
menor = 1000
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
