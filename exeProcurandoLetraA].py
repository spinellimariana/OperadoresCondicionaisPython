'''
Exercício 26 - Aula 09
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez.
'''
print('***PROCURANDO UMA LETRA NA STRING***')
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A 1a letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1)) #vai procurar a posição mais à direita.
