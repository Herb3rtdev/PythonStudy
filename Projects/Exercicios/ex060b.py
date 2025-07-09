n = int(input('Qual numero deseja fazer o fatorial:'))
c = n
m = 1
while c > 0:
    m *= c
    print('{}'.format(c),end='')
    if c > 1:
        print('x',end='')
    else:
        print('=',end='')
    c -= 1
print(m)

