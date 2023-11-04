def ajuda(comand=''):
    from time import sleep
    while True:
        print('+-' * 20)
        print('        SISTEMA DE AJUDA PYHELP')
        print('+-' * 20)
        comand = str(input('Função ou biblioteca: '))
        if comand == 'fim':
            print('Finalizando...')
            break
        else:
            print('=-' * 20)
            print(print(f'Acessando o manual do comando {comand}...'))
            print('=-' * 20)
            sleep(2)
            print(help(comand))


ajuda()
