n = 0
pares = list()
impares = list()
numeros = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}ª número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
numeros.append(pares)
numeros.append(impares)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')