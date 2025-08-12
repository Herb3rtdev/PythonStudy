from datetime import date
def idade(ano):
    """
    O usuário irá colocar o ano que nasceu e o programa irá calcular sua idade atual-independente do ano atual- e  vai retornar a situação. Se precisa ou nao votar ou se é obrigatório ou não.
    """
    data_atual = date.today()
    i = data_atual.year - ano
    if 18 <= i <= 65:
       return (f'Com {i} anos: VOTO OBRIGATORIO.')
    elif  16 <= i < 18 or i >= 65:
        return (f'Com {i} anos: VOTO OPCIONAL.')
    else:
        return (f'Com {i} anos: NÃO VOTA.')


#programa principal
print('-'*30)
ano = int(input('Em que ano voce nasceu? '))
print(idade(ano))
