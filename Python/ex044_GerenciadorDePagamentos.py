#==================formulario====================#
preT = float(input('Digite o valor do produto: '))
print('Qual será o método de pagamento?\n[1] À vista (10% de desconto)\n[2] À vista no cartão (5% de desconto)\n[3] Em até 2x no cartão (preço normal)\n[4] Em 3x ou mais no cartão (20% de juros)')
esc = int(input('Sua escolha: '))
#================================================#


#===================condicionais=================#
if esc == 1:
    preD = (preT * 10) // 100
    print('O valor do produto sairá por: R${:.2f}'.format(preT - preD))
elif esc == 2:
    preD = (preT * 5) // 100
    print('O valor do produto sairá por: R${:.2f}'.format(preT - preD))
elif esc == 3:
    print('O valor do produto sairá por: R${:.2f}'.format(preT))
elif esc == 4:
    preJ = (preT * 20) // 100
    print('O valor do produto sairá por: R${:.2f}'.format(preT + preJ))
#================================================#


print('Agradecemos pela preferência')