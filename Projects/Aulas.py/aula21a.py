def contador(i, f, p):
    """
    Faz uma contagem em ordem crescente
    :param i: Inicio da contagem
    :param f: Final da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    cont = i
    while cont <= f:
        print(cont,end=' ')
        cont += p
    print('Fim')



help(contador)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)