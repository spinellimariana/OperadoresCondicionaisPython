'''
Exercício 19 - Aula 08
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
print('***SORTEANDO ALUNOS***')
print()
from random import choice
aluno1 = str(input('Primeiro aluno: '))     #deixei explícito que era uma string mas não precisa
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]  #uma lista em Python fica entre colchetes
escolhido = choice(lista)
print('O aluno escolhido é: {}.'.format(escolhido))
