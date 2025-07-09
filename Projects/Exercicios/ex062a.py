print('Gerador de PA')
print('-=-'*10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
contador = 0
contemais = 10
total = 0
while contemais != 0:
    total += contemais
    while contador <= total:
        Nn = n1 + (r * contador)
        print(Nn,end=' -> ')
        contador += 1
    print('Pausa')
    contemais = int(input('Quantos termos voce quer mostrar a mais?'))
print('O total de termos contabilizador foi {}'.format(total))
print('Programa finalizado!')
