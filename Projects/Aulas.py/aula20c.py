def dobra(v):
    v2 = []
    for valor in v:
        dobro = valor * 2
        v2.append(dobro)
    print(f'O dobro da lista é {v2}')

    
def dobral(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

    
def mostralinha():
    print('-'*45)


valores=[7,2,5,0,4]
print(f'A lista normal é {valores}')
dobra(valores)
mostralinha()
numeros = [6, 3, 9, 1, 0, 2]
dobral(numeros)
print(f'A lista normal é {numeros}')
print(f'O dobro da lista é {numeros}')