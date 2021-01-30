'''
Exercício 12 - Aula 07
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
print('***CALCULANDO DESCONTO DE 5%***')
print()
produto = float(input('Digite o valor do produto: R$'))
desconto = produto - (produto * 5 / 100)
print('O valor inicial do produto é R${:.2f}, na promoção com o desconto de 5% seu valor passará a ser R${:.2f}!'.format(produto, desconto))
