def cont1_10():
    print('Contagem de 1 até 10 de 1 em 1')
    for contador in range(1,11,1):
        print(contador,end=' ')
    print('FIM!')


def cont10_0():
    print('Contagem de 10 até 0 de 2 em 2')
    for contador in range(10,-2,-2):
        print(contador,end=' ')
    print('FIM!')


def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1   
    if inicio > fim:
        if passo > 0:
            passo = - passo
        else:
            passo = passo     
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    for contador in range(inicio,fim-1,passo):
        print(contador, end=' ')
    print('FIM!')





cont1_10()
cont10_0()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
