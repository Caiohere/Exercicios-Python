trabalhador = {}
condi = 0
trabalhador["nome"] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
ida = 2023 - nasc
trabalhador["idade"] = ida
trabalhador["cpts"] = int(input('Carteira de trabalho(0 não tem): '))
if trabalhador["cpts"] != 0:
    condi = 1
    trabalhador["contrato"] = int(input('Ano de contração: '))
    trabalhador["salario"] = int(input('Salário: '))
    trabalhador["aposentadoria"] = (trabalhador["contrato"] + 35) - nasc
print('=' * 50)
print(trabalhador)
print('Nome: {}'.format(trabalhador["nome"]))
print('Idade: {}'.format(trabalhador["idade"]))
print('CPTS: {}'.format(trabalhador["cpts"]))
if condi == 1:
    print('Ano de contratação: {}'.format(trabalhador["contrato"]))
    print('Salário: {}'.format(trabalhador["salario"]))
    print('Ano da aposentadoria: {}'.format(trabalhador["aposentadoria"]))
