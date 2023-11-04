nome = str(input('Digite seu nome completo: '))
nomeDiv = nome.split()
prim = nomeDiv[0]
ult = nomeDiv[len(nomeDiv)-1]
print('{}\nPrimeiro nome: {}\nSegundo nome: {}'.format(nome, prim, ult))
