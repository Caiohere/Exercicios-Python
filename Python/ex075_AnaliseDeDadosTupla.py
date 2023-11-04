lis = []
num = ()
esc = 0
con = 0
par = []
for c in range(0, 4):
    con += 1
    esc = int(input(f'Digite o {con} valor: '))
    if esc % 2 == 0:
        par.append(esc)
    lis.append(esc)
    esc = 0
num = tuple(lis)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
count3 = num.count(3)
if count3 >= 1:
    print(f'O número 3 apareceu na posição {num.index(3) + 1}ª')
else:
    print('O número 3 não foi digitado em nenhuma posição')
if len(par) == 0:
    print('Não houve valores pares digitados')
else:
    print(f'Os valores pares digitados foram {par}')
