#Escobo global e local
def teste(a):
    #Escopo local
    global b
    b += 5
    c = 2
    print(f'A dentro vale {b}')
    print(f'C dentro vale {c}')


#Escobo global
a = 5
b = 4
teste(a)
teste(b)
print(f'A fora vale {a}')
print(f'B vale {b}')