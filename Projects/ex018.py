from math import cos,tan,sin,radians
angulo = float(input('Digite um angulo:'))
cose = cos(radians(angulo))
tanag = tan(radians(angulo))
seno = sin(radians(angulo))
print('Cosseno {:.2f}\n Seno {:.2f}\n Tangente {:.2f}\n'.format(cose,seno,tanag))

