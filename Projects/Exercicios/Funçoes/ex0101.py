def voto(ano_nascimento):
    """
    :param ano_nascimento: Vai vim para a função o ano que a pessoal nasceu
    :return: resultado do calculo da idade além disso vai retornar se a pessoa está apta ou não para votar 
    """
    
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
       return f'Com {idade}: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: VOTO OPCIONAL'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO'
    

ano_nascimento = int(input('Em que ano voce nasceu? '))
print(voto(ano_nascimento))