'''
Exercício 30 - Aula 10
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print('***PAR OU ÍMPAR?***')
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número digitado é PAR!')
else:
    print('O número digitado é ÍMPAR!')