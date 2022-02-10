from datetime import date
def voto(nasc):
    idade = date.today().year - nasc
    situacao = None
    if idade < 16:
        situacao = 'NÃO VOTA'
    elif 65 > idade >= 18:
        situacao = 'VOTO OBRIGATORIO'
    elif 18 > idade >= 16:
        situacao = 'VOTO OPCIONAL'
    return f'Com {idade} anos: {situacao}.'


print('-'*30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))