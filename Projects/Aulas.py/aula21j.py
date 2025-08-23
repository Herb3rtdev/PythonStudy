#Calcular se um numero é par com funcao-22/08/2025
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


numero = int(input('Digite um numero: '))
if par(numero):
    print('O número é par')
else:
    print('O número é ímpar')