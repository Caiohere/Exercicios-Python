import random
player = 0
pc = 0
pc = random.randint(0, 10)
c = 0
print('O pc vai pensar em um número aleatório entre 0 e 10, tente acertar!')
player = int(input('Qual n° o PC pensou? '))
while player != pc:
    c = c + 1
    print('Você errou!')
    player = int(input('Tente novamente: '))
print('Resposta CORRETA! Você precisou de {} tentativas para acertar.'.format(c))
