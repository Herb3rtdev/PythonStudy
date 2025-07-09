produtos= ('Lapis','1.75','Borracha','2','Caderno','15.90')
for posicao, itens in enumerate(produtos):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]}',end='...')
    else:
        print(f'R${produtos[posicao]}')
