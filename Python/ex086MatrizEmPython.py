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

print(matriz[0])
print(matriz[1])
print(matriz[2])
