import math
opos = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(opos, adj)
print('O valor da hipotenusa desse triângulo retângulo é de {:.2f}'.format(hip))
