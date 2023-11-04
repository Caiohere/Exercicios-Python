ano = 0
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = 2023 - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Total de pessoas maiores de idade: {}'.format(maior))
print('Total de pessoas menores de idade: {}'.format(menor))
print('FIM')