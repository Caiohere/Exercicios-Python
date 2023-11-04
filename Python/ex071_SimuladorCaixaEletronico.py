valor = int(input('Qual valor você quer sacar? '))
total = valor
cedAtual = 50
totalCed = 0
while True:
    if total >= cedAtual:
        total = total - cedAtual
        totalCed += 1
    else:
        if total > 0:
            print('O total {} cedulas de {}'.format(totalCed, cedAtual))
        if cedAtual == 50:
            cedAtual = 20
        elif cedAtual == 20:
            cedAtual = 10
        elif cedAtual == 10:
            cedAtual = 1
        totalCed = 0
        if total == 0:
            break
print('FIM')
