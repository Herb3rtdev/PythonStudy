def fatorial(número,show=False):
    """
    -> Calcula o Fatorial de um número
    :param número: O número que vai ser calculado o fatorial 
    :param show: (opcional) se for True vai calcular e mostrar os numeros calculados. Já se for False vai calcular apenas o resultado
    :return: O resultado do fatorial do número escolhido
    """
    f = 1
    print('-'*25)
    for contador in range(número,0,-1):
        f *= contador
        if show:
            print(contador,end='')
            if contador == 1:
                print(' = ',end='')
            else:
                print(' x ',end='')            
    return f


print(fatorial(5, show = False))