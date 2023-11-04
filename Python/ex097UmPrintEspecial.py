def escreva(texto):
    t = len(texto) + 4
    print('~' * t)
    print(f'  {texto}')
    print('~' * t)


msg = str(input('Mensagem: '))
escreva(msg)

