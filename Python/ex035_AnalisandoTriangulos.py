a = float(input('Digite o comprimento da 1° reta: '))
b = float(input('Digite o comprimento da 2° reta: '))
c = float(input('Digite o comprimento da 3° reta: '))
if a + b > c and a + c > b and b + a > c and b + c > a and c + a > b and c + b > a:
    print('Esses valores podem formar um triângulo.')
else:
    print('Esses valores não podem formar um triângulo.')
print('Fim')