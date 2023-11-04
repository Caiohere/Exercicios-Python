#====================formulario==========================#
nasc = int(input('Qual o ano de nascimento do atleta? '))
#========================================================#

ano = 2023 - nasc

#==============condicionais==============#
if ano > 1 and ano <= 9:
    print('Sua categoria é a MIRIM')
elif ano > 1 and ano <= 14:
    print('Sua categoria é a INFANTIL')
elif ano > 1 and ano <= 19:
    print('Sua categoria é a JUNIOR')
elif ano > 1 and ano <= 20:
    print('Sua categoria é a Sênior')
else:
    print('Sua categoria é a MASTER')
#========================================#

print('Fim')