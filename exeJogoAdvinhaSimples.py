'''
Exercício 28 - Aula 10
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
print('***JOGO DA ADVINHAÇÃO***')
from random import randint
from time import sleep
numero = randint(0, 5) #sortei o número
print('\nVou pensar em um número de 0 a 5, tente advinhar! Qual número eu pensei?')
tentativa = int(input('Digite um número inteiro entre 0 e 5: '))
print('\nPROCESSANDO...')
sleep(3)
if tentativa == numero:
    print('\nParabéns, você venceu!')
else:
    print('\nGAME-OVER!!')
print('O número que o computador pensou foi:', numero)
