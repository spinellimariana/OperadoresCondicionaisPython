'''
Exercício 5 - Aula 07
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
'''
print('***MOSTRANDO O SUCESSOR E O ANTECESSOR DE UM NÚMERO INTEIRO***')
print()
n = int(input('Digite um número qualquer: '))
print('O antecessor de {} é {}; \nO sucessor de {} é {}.'.format(n, (n-1), n, (n+1)))

