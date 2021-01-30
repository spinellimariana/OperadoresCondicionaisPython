'''
Exercício 27 - Aula 09
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
print('***MOSTRANDO PRIMEIRO E ÚLTIMO NOME***')
nome = str(input('\nDigite seu nome completo: ')).strip().split()
print('\nMuito prazer em te conhecer!')
print('Seu primeiro nome é: {}.'.format((nome[0])))
print('Seu último nome é: {}.'.format(nome[len(nome)-1]))
