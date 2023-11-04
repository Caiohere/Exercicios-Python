import random
c = 0
win = 1
p_n = 0
p_esc = ''
pc_esc = ''
pc_n = random.randint(1, 10)
soma = 0
i_p = ''
print('========================')
print('Jogo do par ou ímpar!!')
print('========================')
while win == 1:
    p_n = int(input('digite um número: '))
    p_esc = str(input('Par ou ímpar? [P/I] ').upper())
    soma = p_n + pc_n
    if soma % 2 == 0:
        i_p = 'PAR'
    else:
        i_p = 'ÍMPAR'
    if p_esc == 'P':
        p_esc = 'PAR'
    elif p_esc == 'I':
        p_esc = 'ÍMPAR'
    if p_esc == 'PAR':
        pc_esc = 'ÍMPAR'
    elif p_esc == 'ÍMPAR':
        pc_esc = 'PAR'
    if i_p == p_esc:
        print('========================================================================================')
        print('Você jogou {} e o computador jogou {}. Total de {} DEU {}'.format(p_n, pc_n, soma, i_p))
        print('Você ganhou!!')
        print('Vamos jogar denovo...')
        print('========================================================================================')
        c += 1
        pc_n = random.randint(1, 10)
    else:
        print('========================================================================================')
        print('Você jogou {} e o computador jogou {}. Total de {} DEU {}'.format(p_n, pc_n, soma, i_p))
        print('Você perdeu!!!')
        print('GAMEOVER! Você ganhou {} vezes.'.format(c))
        print('========================================================================================')
        break
