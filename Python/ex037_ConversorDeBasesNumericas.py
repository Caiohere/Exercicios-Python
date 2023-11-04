#=============Formulário==================#
num = int(input('Digite um número inteiro: '))
print('Escolha qual base de conversão: ')
print('[1] CONVERTER PARA BINÁRIO')
print('[2] CONVERTER PARA OCTAl')
print('[3] CONVERTER PARA HEXDECIMAL')
opcao = int(input('Sua opção: '))
#=========================================#

#=======Condicionais===================#
if opcao == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Digite um valor válido.')
print('Fim')