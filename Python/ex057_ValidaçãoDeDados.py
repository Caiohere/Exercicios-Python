sexo = str(input('Digite seu sexo\n[M] para masculino e [F] para feminino: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('ERRO. Digite os dados corretos\nDigite seu sexo: ')).strip().upper()[0]
print('Dados coletados.')