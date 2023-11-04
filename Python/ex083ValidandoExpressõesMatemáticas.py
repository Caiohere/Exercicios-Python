expDivi = list()
exp = str(input('Digite a expressão: '))
for p, l in enumerate(exp):
    expDivi.append(l)
paren1 = expDivi.count('(')
paren2 = expDivi.count(')')
paren = paren1 + paren2
if expDivi[-1] == '(':
    print('A expressão está errada!')
elif expDivi[0] == ')':
    print('A expressão está errada!')
elif paren % 2 == 0:
    print('A expressão é válida!')
else:
    print('A expressão está errada!')
