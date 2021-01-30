'''
Exercício 33 - Aula 10
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print('***MAIOR E MENOR NÚMERO***')
n1 = int(input('\nDigite o 1o valor: '))
n2 = int(input('Digite o 2o valor: '))
n3 = int(input('Digite o 3o valor: '))

#VERIFICANDO O MAIOR:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#VERIFICANDO O MENOR:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O MAIOR número é {}.'.format(maior))
print('O MENOR número é {}.'.format(menor))
