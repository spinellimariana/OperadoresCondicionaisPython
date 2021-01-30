'''
Exercício 20 - Aula 08
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
print('***SORTEANDO ORDEM DE APRESENTAÇÃO DE UM TRABALHO***')
print()
import random
aluno1 = (input('Primeiro aluno: '))     #deixei explícito que era uma string mas não precisa
aluno2 = (input('Segundo aluno: '))
aluno3 = (input('Terceiro aluno: '))
aluno4 = (input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]  #uma lista em Python fica entre colchetes
random.shuffle(lista)                                           #ATENÇÃO: funciona tipo o collections shuffle no java
print('A ordem de apresentação será: {}!'.format(lista))

