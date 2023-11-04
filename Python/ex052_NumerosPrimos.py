npri = 0
n1 = int(input('Digite um número inteiro: '))
for c in range(2, n1-1):
    if n1 % c == 0:
        npri = 1
if npri == 1:
    print('Não é um numero primo')
else:
    print('É um numero primo')
