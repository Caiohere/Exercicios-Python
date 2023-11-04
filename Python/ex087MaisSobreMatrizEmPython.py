matriz = list()
linha0 = list()
linha1 = list()
linha2 = list()

linha0.append(int(input('Digite um valor para [0, 0]: ')))
linha0.append(int(input('Digite um valor para [0, 1]: ')))
linha0.append(int(input('Digite um valor para [0, 2]: ')))

linha1.append(int(input('Digite um valor para [1, 0]: ')))
linha1.append(int(input('Digite um valor para [1, 1]: ')))
linha1.append(int(input('Digite um valor para [1, 2]: ')))

linha2.append(int(input('Digite um valor para [2, 0]: ')))
linha2.append(int(input('Digite um valor para [2, 1]: ')))
linha2.append(int(input('Digite um valor para [2, 2]: ')))

matriz.append(linha0)
matriz.append(linha1)
matriz.append(linha2)
print('=' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=' * 30)
somaP = 0
for n in linha0:
    if n % 2 == 0:
        somaP += n
for n in linha1:
    if n % 2 == 0:
        somaP += n
for n in linha2:
    if n % 2 == 0:
        somaP += n
print(f'A soma dos valores pares é {somaP}')
terS = linha0[2] + linha1[2] + linha2[2]
print(f'A soma dos valores da terceira coluna é {terS}')
print(f'O maior valor da segunda linha é {max(linha1)}')
