#===========formulário============================#
ano = int(input('Digite seu ano de nascimento: '))
#=================================================#

idade = 2023 - ano

#===========Condicionais===============#
if idade < 18:
    falt = idade - 18
    print('Ainda não chegou sua hora de se alista. Ainda falta(m) {} ano(s)'.format(falt * -1))
elif idade == 18:
    print('Chegou seu ano de alistamento, vá a uma junta militar mais próxima.')
elif idade > 18:
    atras = idade - 18
    print('A sua hora de se alistar já se passou! Você está atrasado em {} ano(s)'.format(atras))
print('Fim')