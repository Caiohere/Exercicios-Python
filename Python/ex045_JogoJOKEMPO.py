import random
#===============formulario===================#
print('Vamos jogar jokenpô!')
print('Escolha sua opção\n[1] Jogar papel\n[2] Jogar tesoura\n[3] Jogar pedra')
esc = int(input('Sua escolha é: '))
#============================================#

escPc = random.randint(1, 3)
print(escPc)

#================condicionais=====================#
if esc == escPc:
    print('O pc jogou o mesmo que vc! Deu empate.')
elif esc == 1 and escPc == 2:
    print('O pc jogou tesoura, que corta seu papel! Pc ganhou.')
elif esc == 2 and escPc == 1:
    print('O pc jogou papel, que é cortado pela sua tesoura! Você ganhou.')
elif esc == 1 and escPc == 3:
    print('O pc jogou pedra, que é embrulhado pelo seu papel! Você ganhou.')
elif esc == 3 and escPc == 1:
    print('O pc jogou papel, que embrulha sua pedra! O Pc ganhou.')
elif esc == 2 and escPc == 3:
    print('O pc jogou pedra, que quebra sua tesoura! O Pc ganhou.')
elif esc == 3 and escPc == 2:
    print('O pc jogou tesoura, que é quebrada pela sua pedra! Você ganhou.')
#==================================================#

print('Obrigado por jogar!')