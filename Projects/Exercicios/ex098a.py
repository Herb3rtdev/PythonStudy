def contador(inicio,fim,passo):
   #Verificacao do passo. Caso for igual a zero será atribuido o valor 1 e caso for negativo será transformado em positivo
    if passo == 0:
        passo =1
    if passo < 0:
        passo = abs(passo)
    #crescente
    if inicio < fim:
        c = inicio
        for c in range(inicio,fim+1,passo):
            print(c,end=' ')
        print('FIM')
    #decrescente
    else:
        c = inicio
        for c in range(inicio,fim-1,-passo):
            print(c,end= ' ')
        print('FIM')


#Programa principal
contador(1,10,1)
contador(10,0,2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)