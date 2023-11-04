sal = float(input('Digite o salário desejado: '))
aum = sal * 15 / 100
nsal = sal + aum
print('O salário de R${:.2f}, com aumento de 15% ficará R${:.2f}'.format(sal, nsal))
