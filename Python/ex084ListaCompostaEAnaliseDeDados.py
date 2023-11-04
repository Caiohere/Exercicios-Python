grupo = list()
pessoas = []
pesos = []
maior = []
menor = []
esc = ''
maxnum = indmaxnum = laco = minnum = indminnum = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    esc = str(input('Quer continuar? [S/N] ').upper())
    if esc == 'N':
        break
    if esc not in 'SN' or esc == '':
        while True:
            esc = str(input('Erro! Tente novamente: [S/N] ').upper())
            if esc == 'N':
                laco = 1
                break
            if esc == 'S':
                break
    if laco == 1:
        break
print(f'Ao todo você cadastrou {len(grupo)} pessoas.')
for p in grupo:
    pesos.append(p[1])
pesos2 = pesos[:]
for c in range(0, 2):
    maxnum = max(pesos)
    indmaxnum = pesos.index(maxnum)
    maior.append(indmaxnum)
    maior.append(maxnum)
    pesos[indmaxnum] = 0
print(f'Os maiores pesos foram {grupo[maior[0]][0]} com {maior[1]}KG e {grupo[maior[2]][0]} com {maior[3]}KG')
for c in range(0, 2):
    minnum = min(pesos2)
    indminnum = pesos2.index(minnum)
    menor.append(indminnum)
    menor.append(minnum)
    pesos2[indminnum] = 999
if len(grupo) == 3:
    print(f'O menor peso foi {menor[1]}KG. Peso de {grupo[menor[0]][0]}')
else:
    print(f'Os menores pesos foram de {grupo[menor[0]][0]} com {menor[1]}KG e {grupo[menor[2]][0]} com {menor[3]}')