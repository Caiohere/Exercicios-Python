vel = float(input('Qual a velocidade do carro? (ex: 80) '))
if vel > 80:
    print('Você está acima da velocidade permitida! Você foi multado.')
    mult = (vel - 80) * 7
    print('Sua multa será debitada em R${}'.format(mult))
else:
    print('Você está no limite.')
print('Boa viagem.')