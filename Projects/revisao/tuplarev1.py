lanches = ('Hamburguer','Suco','Pizza','Pudim')
print(lanches[1])
print(lanches[0:2])
print(len(lanches))
for comida in lanches:
    print(comida)
print(lanches[:-1])   
for comida in lanches:
    print(f'Eu vou comer {comida}')
for cont in range(0,len(lanches)):
    print(f'Eu como {lanches[cont]} na {cont+1} vez')

for posicao, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posicao {posicao} ')

