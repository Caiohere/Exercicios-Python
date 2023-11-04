#===================formulario=======================#
a = float(input('Digite o comprimento da 1° reta: '))
b = float(input('Digite o comprimento da 2° reta: '))
c = float(input('Digite o comprimento da 3° reta: '))
#====================================================#

#===============================condicionais=======================================#
if a + b > c and a + c > b and b + a > c and b + c > a and c + a > b and c + b > a:
    print('Esses valores podem formar um triângulo.')
    if a == b and a == c and b == a and b == c and c == b and c == a:
        print('Esse triângulo é equilátero.')
    elif a == b and b != c or b == c and a != c or a == c and b != a:
        print('Esse é um triângulo Isósceles.')
    elif a != b and a != c and b != a and b != c and c != b and c != a:
        print('Esse é um triângulo escaleno.')
else:
    print('Esses valores não podem formar um triângulo.')
#===================================================================================#

print('Fim')