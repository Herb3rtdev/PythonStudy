#Exercício de fatorial-22/08/2025
def fatorial(numero=1):
    f = 1
    for contador in range(numero,0,-1):
        f *= contador
    return f

numero = int(input('Digite um numero: '))
fat = fatorial(numero)
print(f'O fatorial de {numero} é igual a {fat}')