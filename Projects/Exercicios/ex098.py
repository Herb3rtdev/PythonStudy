from time import sleep


def contador(inicio,fim,passo):
    print('-='*15)
    #Corrige passo caso for negativo ou nulo
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    #Crescente
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        c = inicio
        while c <= fim:
            print(c, end=' ',flush = True)
            sleep(0.2)
            c += passo
        print('Fim')
        print('-='*15)
    #Decrescente
    else:
        print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
        c = inicio
        while c >= fim:
            print(c,end=' ',flush = True)
            sleep(0.2)
            c -= passo
        print('Fim')
        print('-='*15)


#Programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de escolher:')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo: '))
contador(inicio,fim,passo)