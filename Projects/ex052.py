s = 0
print('NUMEROS PRIMOS')
n = int(input('Digite um numero:'))
for c in range(1,n+1):
   if n % c == 0:
       s += 1
       print('\033[31m', end='')
   else:
       print('\033[30m', end='')
   print('{} \033[m'.format(c), end= ' ')
print('\nO numero {} foi divisível {} vezes'.format(n, s))
if s == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele não é PRIMO!')