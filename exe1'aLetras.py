'''
Exercício 24 - Aula 09
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''
print('***VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO***')
cidade = str(input('\nEm que cidade você nasceu? ')).strip()
print(cidade)
print(cidade[:5].upper() == 'Santo')
