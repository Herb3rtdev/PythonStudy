#Funcao que vai calcular os numeros em ordem crescente de 1 em 1
def cont1():
    cont = 1
    while cont <= 10:
        print(cont,end=' ')
        cont += 1
    print('FIM!')


#Função que vai calcular os numeros em orde decrescente em 2 em 2
def cont2():
    cont = 10
    while cont >= 0:
        print(cont,end=' ')
        cont -= 2
    print('FIM!')


#Funçao que vai calcular os numeros em ordem decrescente ou crescente
def cont3(i,f,p):
    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont,end=' ')
            cont += p
        print('FIM!')
    if i > f:
        cont = i
        while cont >= f:
            print(cont,end=' ')
            cont -= p
        print('FIM!')

                 
#Programa principal
cont1()
cont2()
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont3(i,f,p)
