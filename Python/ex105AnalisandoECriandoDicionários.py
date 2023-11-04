def notas(*notas, sit=False):
    """
    Função que retorna números de um aluno em forma
    de dicionário
    :param notas: notas do aluno (quantas necessárias)
    :param sit: se ativa, mostra a situação do aluno (boa ou ruim)
    :return: um dict com as informação do aluno
    """
    aluno = dict()
    aluno["total"] = len(notas)
    aluno["high"] = max(notas)
    aluno["low"] = min(notas)
    aluno["media"] = sum(notas) / aluno["total"]
    if sit:
        if aluno["media"] >= 7:
            aluno["situação"] = 'BOA'
        else:
            aluno["situação"] = 'RUIM'
    return f'{aluno}'


resp = list()
resp = notas(4.0, 10, 6.5, sit=True)
print(resp)
help(notas)



