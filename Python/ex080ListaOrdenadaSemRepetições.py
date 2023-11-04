#EXERCIO COM INTUITO DE SER FEITO SEM A UTILIZAÇÃO DE ESTRUTURAS DE REPETIÇÕES!!!!!
num = list()
n1 = int(input('Digite um valor: '))
num.append(n1)
print('Adicionado ao final da lista...')
n2 = int(input('Digite um valor: '))
if n2 < n1:
    num.insert(0, n2)
    print('Adicionado na posição 0 da lista')
else:
    num.append(n2)
    print('Adicionado ao final da lista...')
n3 = int(input('Digite um valor: '))
if n3 > max(num):
    num.append(n3)
    print('Adicionado ao final da lista...')
elif n3 < min(num):
    num.insert(0, n3)
    print('Adicionado na posição 0 da lista')
else:
    num.insert(1, n3)
    print('Adicionado na posição 1 da lista')
n4 = int(input('Digite um valor: '))
if n4 > max(num):
    num.append(n4)
    print('Adicionado ao final da lista...')
elif n4 < min(num):
    num.insert(0, n4)
    print('Adicionado na posição 0 da lista')
elif n4 > num[1]:
    num.insert(2, n4)
    print('Adicionado na posição 2 da lista')
elif n4 < num[1]:
    num.insert(1, n4)
    print('Adicionado na posição 1 da lista')
n5 = int(input('Digite um valor: '))
if n5 > max(num):
    num.append(n5)
    print('Adicionado ao final da lista...')
elif n5 < min(num):
    num.insert(0, n5)
    print('Adicionado na posição 0 da lista')
elif n5 > num[2]:
    num.insert(3, n5)
    print('Adicionado na posição 3 da lista')
elif n5 < num[2] and n5 > num[1]:
    num.insert(2, n5)
    print('Adicionado na posição 2 da lista')
elif n5 > num[1]:
    num.insert(2, n5)
    print('Adicionado na posição 2 da lista')
elif n5 < num[1]:
    num.insert(1, n5)
    print('Adicionado na posição 1 da lista')
print(num)
