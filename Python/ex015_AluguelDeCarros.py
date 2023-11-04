km = float(input('Quantos KM o carro rodou? '))
dias = int(input('Quantos Dias alugado? '))
pdias = dias * 60
pkm = km * 0.15
total = pdias + pkm
print('O total a pagar é de R${:.2f}'.format(total))
