
n1 = int(input('Digite o 1.o termo:'))
r = int(input('Razão:'))
c = -1
while c < 9:
    c += 1
    n = n1 + (c * r)
    print(n, end=' -> ')
print('\nO décimo termo da PA é {}'.format(n))
