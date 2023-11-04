nome = str(input('Digite seu nome completo: '))
nomeMa = nome.upper()
nomeMi = nome.lower()
espaços = nome.count(' ')
carac = len(nome)
Tletras = carac - espaços
div = nome.split()
div2 = len(div[0])
print('Nome em maiúscula: {}'.format(nomeMa))
print('Nome em minúscula: {}'.format(nomeMi))
print('O n° de letras é de: {}'.format(Tletras))
print('A quantidade de letras do primeiro nome é de: {}'.format(div2))

