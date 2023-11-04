#=========Formulário=========================#
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite o 2° número inteiro: '))
#=============================================#

#===========Condicionais======================#
if n1 > n2:
    print('O primeiro número ({}) é o maior entre os dois.'.format(n1))
elif n2 > n1:
    print('O segundo número ({}) é o maior entre os dois'.format(n2))
else:
    print('Não existe número maior, os dois valores são iguais.')