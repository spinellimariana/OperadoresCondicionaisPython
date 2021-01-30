'''
Exercício 18 - Aula 08
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
print('***SENO, COSSENO E TANGENTE***')
print()
angulo = float(input('Digite o ângulo: '))
import math
seno = math.sin(math.radians(angulo))  #tem que entregar o grau do angulo em radianos por isso precisa do radians
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('Para o ângulo {} temos:\nSeno = {:.2f};\nCosseno = {:.2f};\nTangente = {:.2f}.'.format(angulo, seno, cos, tang))


