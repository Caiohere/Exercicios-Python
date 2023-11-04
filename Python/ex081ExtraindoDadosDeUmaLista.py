num = list()
esc = ''
laco = 0
while True:
    num.append(int(input('Digite um valor: ')))
    esc = str(input('Quer continuar? [S/N]').upper())
    if esc == 'N':
        break
    if esc not in 'SN':
        while True:
            esc = str(input('Erro! Tente novamente: [S/N]').upper())
            if esc == 'N':
                laco = 1
                break
            if esc == 'S':
                break
    if laco == 1:
        break
print(f'A quantidade de valores digitados foram {len(num)}')
num.sort(reverse=True)
print(f'Lista ordenada: {num}')
n5 = num.count(5)
if n5 >= 1:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado, portanto não está na lista')
