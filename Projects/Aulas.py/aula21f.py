def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
    

f = int(input('Fatorial: '))
print(f'O fatorial de {f} é {fatorial(f)}')