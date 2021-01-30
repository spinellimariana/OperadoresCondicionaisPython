from math import pow, pi
print('***COMPARANDO A MAIOR ÁREA***')

lado = float(input('\nInforme o lado do quadrado: '))
raio = float(input('Informe o raio do círculo: '))

quadrado = lado * lado
circulo = (pow(raio, 2)) * pi

if quadrado > circulo:
    print('\nA área do QUADRADO é maior!')
else:
    print('\nA área do CÍRCULO é maior!')
