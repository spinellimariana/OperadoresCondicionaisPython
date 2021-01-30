'''
Exercício 23 - Aula 09
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: digite um número: 1834
unidade: 4, dezena: 3, centena: 8 e milhar 1.
'''
print('***SEPARANDO DÍGITOS DE UM NÚMERO***')
num = int(input('\nInforme um número: '))
print('\nAnalisando o número: {}...'.format(num))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('\nUnidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
