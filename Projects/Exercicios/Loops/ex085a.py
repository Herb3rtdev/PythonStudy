numeros = [[], []]
#Criou listas vazias logo no comeco para nao precisar adicionar via append.[numeros[0]-numeros pares] e numeros[1]-numeros impares
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o valor {c}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*15)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]} ')