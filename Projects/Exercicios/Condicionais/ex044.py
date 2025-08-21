print('{:=^40}'.format('LOJA GATHONES'))
p = float(input('Qual é o preço do produto? R$'))
print('Qual a forma de pagamento?')
print('[1] A vista no dinheiro ou pix com 10% de desconto')
print('[2] A vista no cartao ou cheque com 5% de desconto')
print('[3] Em ate 2x no cartao com Preço normal')
print('[4] 3x ou mais no cartao com 20% de juros')
escolha = int(input('Qual opção voce irá escolher:'))
print('-=-'*14)
if escolha == 1:
   total :float = p * 0.9
elif escolha == 2:
    total : float = p * 0.95
elif escolha == 3:
    total = p
    parcela = total / 2
    print('Sua compra sera parcelada em 2x SEM JUROS de R${}'.format(parcela))
elif escolha == 4:
    parcelas = int(input('Quantas parcelas?'))
    total: float = (p * 1.2)
    totalpar = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,totalpar))
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(p,total))