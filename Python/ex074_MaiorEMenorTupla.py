import random
numT = ()
lis = []
for c in range(0, 5):
    ale = ''
    ale = random.randint(0, 100)
    lis.append(ale)
numT = tuple(lis)
print(f'Os 5 números aleatórios gerados foram: {numT}')
orga = sorted(numT)

print(f'O menor valor {orga[0]} e o maior valor {orga[4]}')
