import math
ang = float(input('Digite o valor do ângulo: '))
cose = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))

print('A partir do ângulo {} obtemos:\n Cosseno {}\n Seno {}\n Tangente {}'.format(ang, cose, seno, tang))

