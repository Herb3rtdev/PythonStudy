n1 = int(input('Digite o primeiro termo:'))
r = int(input('Razao:'))
quantidade_termos = 0
contador = 0
opcoes =''
while contador < 10:
    contador += 1
    Ultimon = n1 + ((contador-1) * r)
    print(Ultimon,end=' -> ')
while not opcoes == 0:
    if opcoes != 0:
        opcoes = int(input('\n-Digite quantos termos que somar\n-Se digitar 0 encerra o programa\n'))
        nT = Ultimon + (r * opcoes)
        print(nT)
        Ultimon = nT
        quantidade_termos += opcoes
print('A quantidade de termos foi {} e o ultimo termo é {}'.format(quantidade_termos + 10, nT))
print('Programa finalizado!')

