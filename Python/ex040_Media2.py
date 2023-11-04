#==========formulario=================#
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
#=====================================#
media = (n1 + n2) // 2

#========condicionais=================#
if media < 5.0:
    print('Média: {}\nREPROVADO'.format(media))
elif media >= 5 and media < 6.9:
    print('Média: {}\nRECUPERAÇÃO'.format(media))
else:
    print('Média: {}\nAPROVADO'.format(media))
#======================================#

print('Fim')