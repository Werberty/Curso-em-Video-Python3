def notas(*n, sit=False):
    """
    -> Função para avaliar a situação de varios alunos
    :param n: uma ou mais notas dos aluno
    :param sit: valor opcional, indica se deve ou não colocar a sitação
    :return: dicionário com várias informaçoes sobre a sitação da turma
    """
    bib = dict()
    soma = 0
    bib['total'] = len(n)
    bib['maior'] = max(n)
    bib['menor'] = min(n)
    bib['média'] = sum(n) / len(n)
    if sit:
        if bib['média'] >= 7:
            bib['situação'] = 'BOM'
        elif bib['média'] < 5:
            bib['situação'] = 'RUIM'
        else:
            bib['situação'] = 'RAZOÁVEL'
    return bib


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)