'''
Exercício 17 - Aula 08
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''
import math
print('***HIPOTENUSA DO TRIÂNGULO***')
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))

hip = math.hypot(oposto, adjacente) #melhor forma, mais simples mais elegante.
print('O comprimento da hipotenusa é {:.2f}!'.format(hip))

hipotenusa = math.sqrt((math.pow(oposto, 2) + math.pow(adjacente, 2)))  #outra forma
print(hipotenusa)

hi = (oposto**2 + adjacente**2) ** (1/2) #sem importação
print(hi)




