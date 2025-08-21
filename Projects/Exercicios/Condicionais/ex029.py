v = int(input('Qual a velocidade do carro:'))
if v > 80:
    print('Infelizmente, voce foi multado por excesso de velocidade. \nA sua multa vai custar R${:.2f}'.format((v-80) * 7))
else:
    print('Sua velocidade está dentro dos parametros. Voce nao será multado.')
