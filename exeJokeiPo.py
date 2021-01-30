'''
Exercício 45 - Aula 12
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
print('***PEDRA, PAPEL E TESOURA***')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('Opções:'
      '\n[0] Pedra;'
      '\n[1] Papel;'
      '\n[2] Tesoura.')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 10)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}.'.format(lista[jogador]))
print('-=' * 10)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
