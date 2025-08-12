def fatorial(n, show = False):
    """
    -> O usuário irá escolher que numero irá fatorar
    -> Depois irá escolhar uma numeraçao que vai caracterizar True ou False. Caso for True, o programa irá calcular como chegou no resultado, já se for False vai mostrar apenas o resultado.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c == 1:
                print(' = ',end=' ')
            else:
                print(' x ',end=' ')
        f *= c
    return f


#Programa principal
while True:
    print('-='*15)
    ft = int(input('Fatorial: '))
    escolha= int(input('[1]- Mostrar como chegou no resultado\n[2]- Mostrar o valor total\n'))
    print('-='*15)
    if escolha == 1:
        escolha = True
    else:
        escolha = False
    print(fatorial(ft, show = escolha))
    print('-='*15)
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'nN':
        break
print('-='*15)
print('Programa Finalizado')