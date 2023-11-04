frase = str(input('Digite uma frase: '))
fraseL = frase.lower()
letraT = fraseL.count('a')
letraA = fraseL.find('a')+1
letraAu = fraseL.rfind('a')+1
print('A letra "a" aparece {} vezes na frase\nA primeira letra "a" aparece na posição {}\nA última letra "a" aparece na posição {}'.format(letraT,letraA,letraAu))
