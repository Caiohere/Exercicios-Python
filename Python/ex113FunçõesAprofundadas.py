def leiaint():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um valor válido.\033[m')
            continue
        else:
            return num


n = leiaint()
print(f'Número {n} selecionado')

print('-=' * 25)


def leiafloat():
    while True:
        try:
            num = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except(ValueError, TypeError):
            print('\033[31mPor favor, digite um número válido.\033[m')
            continue
        else:
            return num


n = leiafloat()
print(f'{n} foi o número selecionado')
