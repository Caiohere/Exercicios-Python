ida = 0
ida18 = 0
sexo = ''
hom = 0
mul20 = 0
esc = 'S'
print('=====================')
print('CADASTRE UMA PESSOA')
print('=====================')
while True:
    ida = int(input('Idade: '))
    if ida >= 18:
        ida18 += 1
    sexo = str(input('Sexo: [M/F] ').upper())
    if sexo == 'M':
        hom += 1
#==================================================#
    if sexo == 'F' and ida < 20:
         mul20 += 1
#==================================================#
    print('==================================')
    esc = str(input('Quer continuar? [S/N] ').upper())
    print('==================================')
    if esc != 'S':
        break
print('Total de pessoas com mais de 18 ano: {}'.format(ida18))
print('Ao todo temos {} homens cadastrados'.format(hom))
print('E temos {} mulheres com menos de 20 anos'.format(mul20))
