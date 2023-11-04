dist = float(input('Quantos KM serão percorridos nessa viagem? '))
if dist <= 200:
    pre = dist * 0.50
    print('O custo da viagem será de R${:.2f}'.format(pre))
else:
    pre = dist * 0.45
    print('O custo da viagem será de R${:.2f}'.format(pre))
print('Tenha uma boa viagem!')