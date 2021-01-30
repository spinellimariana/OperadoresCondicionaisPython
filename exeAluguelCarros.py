'''
Exercício 15 - Aula 07
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
print('***ALUGUEL DE CARROS***')
dias = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))
total = (dias * 60) + (km*0.15)
print('Total a pagar: R${:.2f}'.format(total))

