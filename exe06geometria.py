import math
print('***CÁLCULOS GEOMÉTRICOS***')
a = float(input('\nDigite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
triangulo = (a * c)/2                       #letra a
circulo = (math.pow(c, 2)) * math.pi        #letra b
trapezio = ((a + b) * c) / 2                #letra c
quadrado = math.pow(b, b)                   #letra d
retangulo = a * b                           #letra e
perimetro = (2 * a) + (2 * b)               #letra f
print('\nÁrea do Triângulo Retângulo: {:.2f}.'.format(triangulo))
print('Área do Círculo: {:.2f}.'.format(circulo))
print('Área do Trapézio: {:.2f}'.format(trapezio))
print('Área do Quadrado: {:.2f}.'.format(quadrado))
print('Área do Retângulo: {:.2f}.'.format(retangulo))
print('Perímetro do Retângulo: {:.2f}.'.format(perimetro))
