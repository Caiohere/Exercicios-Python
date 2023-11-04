def area(largura, comprimento):
    a = largura * comprimento
    print('A área do terreno {}x{} é de {}m²'.format(largura, comprimento, a))


print('  CONTROLE DE TERRENOS  ')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)


