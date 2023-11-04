def leiaint(msg='', num=0):
    print(msg, end='')
    num = input('')
    while True:
        if num.isnumeric():
            return f'Você digitou o número {num}'
        else:
            num = input('Erro! Digite novamente: ')


n = leiaint('Digite um número inteiro: ')
print(f'{n}')
