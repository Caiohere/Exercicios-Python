grupo = []
pessoa = {}
ida = 0
while True:
    pessoa["nome"] = str(input('Nome: '))
    pessoa["sexo"] = str(input('Sexo: [M/F] ').upper())
    pessoa["idade"] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    pessoa.clear()
    esc = str(input('Quer continuar?[S/N] '))
    if esc in 'Nn':
        break
print(grupo)
print('-=' * 30)
print('Ao todo foram cadastradas {} pessoas.'.format(len(grupo)))
for i in grupo:
    ida += i["idade"]
print('A média idade do grupo é de {}.'.format(ida // len(grupo)))
print('As mulheres cadastradas foram: ')
for p in grupo:
    if p["sexo"] == 'F':
        print('- {}'.format(p["nome"]))
print('Lista das pessoas que estão acima da média:')
for h in grupo:
    if h["idade"] > ida // len(grupo):
        print('- nome = {}; sexo = {}; idade {};'.format(h["nome"], h["sexo"], h["idade"]))
