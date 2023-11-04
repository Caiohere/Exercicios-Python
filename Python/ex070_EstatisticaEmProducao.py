nome = []
preL = []
pre = 0
preT = 0
preK = 0
esc = ' '
menor = 0
locM = 0
while True:
    print('========================================')
    nome.append(str(input('Digite o nome do produto: ').upper().strip()))
    pre = int(input('Agora digite seu preço: ').strip())
    preL.append(pre)
    preT += pre
    if pre >= 1000:
        preK += 1
    menor = min(preL)
    locM = preL.index(menor)
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ').strip().upper())[0]
    if esc == 'N':
        break
    esc = ' '
print('===========================================')
print('O gasto total foi de {}'.format(preT))
print('Ao todo foram {} produtos a cima de R$1000'.format(preK))
print('O menor preço foi o {}, por R${}'.format(nome[locM], menor))
print(menor)
print('===========================================')
