#================Formulário========================#
vcasa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do salário? '))
pres = int(input('Quantos anos de prestações? '))
#==================================================#

#====Prestações e salário=====#
mes = pres * 12
presM = vcasa // mes
salP = (sal * 30) // 100
#=============================#

#Condicionais
if presM > salP:
    print('Empréstimo negado! Para pagar uma casa de R${:.3f} em {} anos, a mensalidade seria de R${:.2f}\nO valor mesal excede 30% do salário. '.format(vcasa, pres, presM))
else:
    print('Empréstimo liberado! Para pagar uma casa de R${:.3f} em {} anos, a mensalidade será de R${:.2f}'.format(vcasa, pres, presM))
print('Fim')