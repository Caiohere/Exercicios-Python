esc = ''
num = []
laco = 0
while True:
    n = int(input('Digite um valor: '))
    if num.count(n) >= 1:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        num.append(n)
    esc = str(input('Quer continuar? [S/N] ').upper())
    if esc == 'N':
        break
    if esc not in 'SN':
        while True:
            esc = str(input('Erro! Digite novamente [S/N]').upper())
            if esc == 'N':
                laco = 1
                break
            if esc == 'S':
                break
    if laco == 1:
        break
print(sorted(num))
