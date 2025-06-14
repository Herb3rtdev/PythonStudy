f = int(input('Fatorial:'))
m = 1
for c in range (1,f+1):
    m *= c
print('O fatoria de {}! é igual a {}'.format(f,m))