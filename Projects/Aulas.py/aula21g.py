def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um numero: '))
print(par(num))
if par(num) == True:
    print('É par')
else:
    print('É impar')