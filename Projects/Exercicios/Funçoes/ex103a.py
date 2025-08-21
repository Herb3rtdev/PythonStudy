def ficha(n='<desconhecido>',g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


#Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
#Como o parametro gols é inteiro ele daria problema no programa. Entao atribuimos o parametro de string para funcionar. Logo em seguida é feita uma verificaçao se gols é numero, caso sim o parametro muda para inteiro e dessa maneira nao da erro.
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
#Caso o nome nao seja preeenchido levaremos em conta apenas o numeros gols que caso nao for preenchido ou preenchido errado será atribuido valor zero
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome,gols)