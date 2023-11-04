nome = str(input('Digite o nome da cidade: '))
nomeMa = nome.upper()
nomeDiv = nomeMa.split()
sn = 'SANTO' in nomeDiv[0]
print('O nome essa cidade começa com "santo"?: {}'.format(sn))
