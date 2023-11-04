classe = []
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'média de {aluno["nome"]}: '))
if aluno["média"] >= 7:
    aluno["situação"] = 'Aprovado'
else:
    aluno["situação"] = 'Reprovado'

print('Nome é igual a {}'.format(aluno["nome"]))
print('Média é igual a {}'.format(aluno["média"]))
print('Situação é igual a {}'.format(aluno["situação"]))