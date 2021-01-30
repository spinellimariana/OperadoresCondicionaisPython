'''
Exercício 13 - Aula 07
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
print('***REAJUSTE SALARIAL***')
print()
salário = float(input('Digite o salário do funcionário: '))
reajuste = salário + (salário * 15/100)
print('O salário inicial era de R${:.2f}, com o reajuste de 15% passou a ser de R${:.2f}!'.format(salário, reajuste))
