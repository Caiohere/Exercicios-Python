anoatual = 2023


def voto(ano):
    global anoatual
    idade = anoatual - ano
    print(f'com {idade} anos: ', end='')
    if idade < 16:
        return 'Não pode votar!'
    elif 16 <= idade < 18:
        return 'A votação é opcional!'
    elif 18 <= idade <= 65:
        return 'Votação obrigatória!'
    elif idade >= 65:
        return 'A votação é opcional'


resp = int(input('Qual ano do seu nascimento? '))
print(voto(resp))
