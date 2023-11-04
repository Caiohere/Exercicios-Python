idadesT = 0
nomesH = []
nomesM = []
idadesH = []
idadesM = []
nomeH = ''
nomeM = ''
velho = 0
idadeH = 0
idadeM = 0
sexo = 0
vinteM = 0
for c in range(1, 5):
    print('#======================================================#')
    print('Digite abaixo as informações da {}ª pessoa: '.format(c))
    print('Sexo\n[1] Homem\n[2] Mulher')
    sexo = int(input('Escolha: '))
    if sexo == 1:
        nomeH = str(input('Nome: '))
        nomesH.append(nomeH)
        idadeH = int(input('Idade: '))
        idadesH.append(idadeH)
        if c == 1:
            velho = idadeH
        if idadeH > velho:
            velho = idadeH

    elif sexo == 2:
        nomeM = str(input('Nome: '))
        nomesM.append(nomeM)
        idadeM = int(input('Idade: '))
        idadesM.append(idadeM)
        if idadeM < 20:
            vinteM = vinteM + 1
print('#======================================================#')
idadesT = idadesH + idadesM
loc = idadesH.index(velho)
print('A média de idade do grupo é de {} anos'.format(sum(idadesT) / 4))
print('O homem mais velho é o {}, com {} anos de idade.'.format(nomesH[loc], velho))
print('Existem {} mulheres com menos de 20 anos.'.format(vinteM))
