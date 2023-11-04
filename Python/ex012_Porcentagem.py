pp = float(input('Digite o preço do produto: '))
desc = pp * 5 / 100
npp = pp - desc
print('O produto com preço inicial de R${}, ficará R${} com 5% de desconto.'.format(pp, npp))
