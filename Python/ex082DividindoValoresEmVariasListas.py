numT = list()
numP = list()
numI = list()
laco = 0
esc = ''
while True:
    numT.append(int(input('Digite um valor: ')))
    esc = str(input('Quer continuar? [S/N] ').upper())
    if esc == 'N':
        break
    if esc not in 'SN':
        while True:
            esc = str(input('Erro! Tente novamente [S/N] ').upper())
            if esc == 'N':
                laco = 1
                break
            if esc == 'S':
                break
    if laco == 1:
        break
for p, v in enumerate(numT):
    if v % 2 == 0:
        numP.append(v)
    else:
        numI.append(v)
print(f'A lista completa é {numT}')
print(f'A lista de pares é {numP}')
print(f'A lista de ímpares é {numI}')
