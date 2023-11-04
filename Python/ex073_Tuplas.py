times = ('CORINTHIANS', 'PALMEIRAS', 'SANTOS', 'GRÊMIO',
         'CRUZEIRO', 'FLAMENGO', 'VASCO DA GAMA', 'CHAPECOENSE', 'ATLÉTICO-MG',
         'BOTAFOGO', 'ATHLETICO-PR', 'BAHIA', 'SÃO PAULO',
         'FLUMINENSE', 'SPORT', 'VITÓRIA', 'CORITIBA', 'AVAÍ',
         'PONTE PRETA', 'ATLÉTICO-GO')
print('BRASILEIRÃO 2017')
print(f'Os 5 primeiros colocados: {times[:5]}')
print(f'Os 4 últimos colocados: {times[-4:]}')
print(f'Todos os times em ordem alfabética: {sorted(times)}')
chap = times.index('CHAPECOENSE')
print(f'A Chapecoense está em {chap + 1}° colocado')