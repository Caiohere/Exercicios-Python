sal = float(input('Digite o valor salário do funcionário: '))
if sal > 1250:
    aum = (sal * 10) // 100
    salN = sal + aum
    print('Novo salário de R${:.2f} com 10% de aumento.'.format(salN))
else:
    aum = (sal * 15) // 100
    salN = sal + aum
    print('Novo salário de R${:.2f} com 15% de aumento.'.format(salN))
print('Fim')