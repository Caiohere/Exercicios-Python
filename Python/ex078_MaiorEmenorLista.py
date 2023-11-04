num = []
num1 = num[:]
c = 1
count = 0
for c in range(1, 6):
    num.append(int(input(f'Digite o {c}ª valor: ')))
    num1 = num[:]
print(f'Os valores digitados foram {num}')
print(f'O maior valor da lista é {max(num)} nas posições', end=' ')
ma = max(num)
me = min(num)
while True:
    if ma in num:
        print(num.index(ma), end='...')
        num[num.index(ma)] = '-'
    if ma not in num:
        break
print(f'\nO menor valor da lista é {min(num1)} nas posições', end=' ')
while True:
    if me in num:
        print(num.index(me), end='...')
        num[num.index(me)] = '-'
    if me not in num:
        break
