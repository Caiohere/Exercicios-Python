n1 = 0
n2 = 0
soma = 0
mult = 0
esc = 0
n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
esc = int(input('Sua escolha: '))
while esc != 5:
    if esc == 1:
        soma = n1 + n2
        print('============================================')
        print('O resultado da soma dos dois número é de {}'.format(soma))
        print('============================================')
        esc = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: '))
    elif esc == 2:
        mult = n1 * n2
        print('============================================')
        print('O resultado da multiplicação dos dois número é de {}'.format(mult))
        print('============================================')
        esc = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: '))
    elif esc == 3:
        if n1 > n2:
            print('============================================')
            print('O 1° número é o maior.')
            print('============================================')
        else:
            print('============================================')
            print('O 2° número é o maior.')
            print('============================================')
        esc = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: '))
    elif esc == 4:
        n1 = 0
        n2 = 0
        print('Digite os números novamente')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
        esc = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: '))
if esc == 5:
    print('Tchau!')
