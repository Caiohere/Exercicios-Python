from num2words import num2words
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
esc = 0
print(num)
exten = ''
cont = 0
while True:
    esc = int(input('Digite um número entre 0 e 20: '))
    exten = num2words(esc, lang='pt-br')
    cont = num.count(esc)
    if cont >= 1:
        print(f'Você digitou o número {exten}')
        break
    if cont == 0:
        laço = 1
        while cont == 0:
            esc = 0
            esc = int(input('Tente novamente. Digite um número entre 0 e 20: '))
            cont = num.count(esc)
            exten = num2words(esc, lang='pt-br')
            if cont >= 1:
                print(f'Você digitou o número {exten}')
                break
    if laço == 1:
        break