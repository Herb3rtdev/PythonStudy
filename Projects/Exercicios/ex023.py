n = int(input('Digite um numero:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhar:{}'.format(m))

