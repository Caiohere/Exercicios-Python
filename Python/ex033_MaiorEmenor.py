n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
if n1 > n2 and n1 > n3:
    print('O primeiro número é o maior entre os três.')
elif n2 > n1 and n2 > n3:
    print('O segundo número é o maior entre os três.')
else:
    print('O terceiro número é o maior entre os três.')
print('Fim')