'''
Exercício 36 - Aula 12
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('***FINANCIMENTO IMOBILIARIO***')
casa = float(input('\nQual o valor da casa que você pretende comprar? R$ '))
anos = int(input('Quantos anos você pretende pagar? '))
salario = float(input('Informe seu salário: R$ '))

renda = salario * 30 / 100
prestacao = casa / (12 * anos)

print('\nValor da prestação: R$ {:.2f}'.format(prestacao))
if prestacao >= renda:
    print('\n\033[1;31mEMPRÉSTIMO NEGADO!\033[m\nA prestação mensal excede 30% do seu salário!')
else:
    print('\n\033[1;32mPARABÉNS, EMPRÉSTIMO APROVADO!\033[m')
