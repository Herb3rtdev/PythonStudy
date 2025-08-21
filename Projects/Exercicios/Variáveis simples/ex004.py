
coisa = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(coisa))
print('É um numero?', coisa.isnumeric())
print('É uma letra?', coisa.isalpha())
print('Só tem espaços?',coisa.isspace())
print('Sao letras maiusculas?',coisa.isupper())
print('Sao letras minusculas?',coisa.islower())
print('Está misturada maiusculas e minusculas, ou seja capitalizada?',coisa.istitle())
print('Tem numero e letras?',coisa.isalnum())

