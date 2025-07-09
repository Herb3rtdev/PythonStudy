from random import choice
n1 = str(input('Digite o 1.o nome: '))
n2 = str(input('Digite o 2.o nome: '))
n3 = str(input('Digite o 3.o nome: '))
n4 = str(input('Digite o 4.o nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))

