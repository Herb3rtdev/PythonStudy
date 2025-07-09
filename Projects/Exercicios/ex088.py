from random import randint
jogos = []
mega_sena = [] 
contador = 0
resp = int(input('Quantos jogos voce quer que eu sorteie?'))
while resp > contador:
    while len(jogos) < 6:
        numeros = randint(1,60)
        if numeros not in jogos:
            jogos.append(numeros)
    jogos.sort()
    mega_sena.append(jogos[:])
    jogos.clear()
    contador += 1
for posicao,jogo in enumerate(mega_sena):
    print(f'Jogo {posicao+1}: {mega_sena[posicao]}')
    