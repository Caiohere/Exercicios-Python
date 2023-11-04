frase = str(input('Digite uma frase e direi se ela é palindromo: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('{} de tras para frente é {}, ou seja, essa é uma frase palindromo'.format(junto, inverso))
else:
    print('{} de tras para frente é {}, ou seja, essa não é uma frase palindromo'.format(junto, inverso))

print('FIM')