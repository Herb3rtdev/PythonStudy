def fatorial(num=1):
    f = 1
    cont = num
    while cont > 0:
        f *= cont 
        cont -= 1
    return f



f = int(input('Fatorial: '))
print(f'O fatorial de {f} é {fatorial(f)}')