'''
Exercício 25 - Aula 09
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''
print('***SILVA NO NOME***')
nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome tem Silva? {}.'.format('SILVA' in nome))
