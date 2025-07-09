n1= int(input('Digite 1.o numero:'))
n2= int(input('Digite 2.o numero:'))
print('-=-'*10)
op = ''
while not op == '5':
    op = input('[1]Soma\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\n')
    if op == '1':
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,n1+n2))
    elif op == '2':
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,n1*n2))
    elif op == '3':
        if n1 > n2:
            maior = n1
            print('O maior numero é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior numero é {}'.format(maior))
        else:
            print('Os dois são iguais!')
    elif op == '4':
        n1 = int(input('Digite 1.o numero:'))
        n2 = int(input('Digite 2.o numero:'))
    elif op == '5' :
        print('Programa finalizado!')
    else:
        print('Opção inválida! Tente novamente!')


