'''
Exercício 16 - Aula 08
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
ex. digitando o número 6,123, imprime 6.
'''
from math import trunc
print('***MOSTRANDO APENAS A PORÇÃO INTEIRA DO NÚMERO***')
print()
n = float(input('Digite um número: '))
print('O número digitado é {} e sua porção inteira é {}!'.format(n, trunc(n)))
print('O número digitado é {} e sua porção inteira é {}!'.format(n, int(n)))
#também dá pra fazer com essa função interna sem importação do math trunc

