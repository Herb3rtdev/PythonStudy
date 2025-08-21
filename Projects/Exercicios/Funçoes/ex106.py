from math import sqrt
def delta(a,b,c):
    delta = (b **2 - (4 * a * c))
    print(f'O valor de delta é {delta} e',end=' ')
    if delta == 0:
        print('Existe apenas uma raiz')
        return baskara(delta,a,b)
    elif delta > 0:
        print('Existe duas raízes')
        return baskara(delta,a,b)
    else:
        print('Não existe raiz nos números reais')
        return 'Programa finalizado'


def baskara(delta,a,b):
    if delta > 0:
        raiz = sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a) 
        print(f'A raízes são {x1} e {x2}')
    elif delta == 0:
         x = -b / (2 * a)
         print(f'A única raiz é {x}')



a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta(a,b,c)
