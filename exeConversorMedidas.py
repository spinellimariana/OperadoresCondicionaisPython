'''
Exercício 08 - Aula 07
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''
print('***CONVERSOR DE MEDIDAS***')
print()
n = float(input('Valor em metros: '))
print('Valor em metros: {}; \nValor em centímetros: {:.0f}cm; \nValor em milímetros: {:.0f}mm.'.format(n, (n*100), (n*1000)))
