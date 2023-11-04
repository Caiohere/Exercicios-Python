pala = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'ESTUDAR')
c = 0
vog = []
let = ''
for c in range(0, 6):
    if 'A' in pala[c]:
        let = 'a'
        vog.append(let)
    if 'E' in pala[c]:
        let = 'e'
        vog.append(let)
    if 'I' in pala[c]:
        let = 'i'
        vog.append(let)
    if 'O' in pala[c]:
        let = 'o'
        vog.append(let)
    if 'U' in pala[c]:
        let = 'u'
        vog.append(let)
    print(f'Na palavra {pala[c]} temos {vog}')
    vog = []
