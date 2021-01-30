'''
Exercício 34 - Aula 10
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
print('***AUMENTO SALARIAL***')
salario = float(input('\nInforme seu salário: '))

if salario <= 1250:
    aumento = salario + (salario * 15)/100
else:
    aumento = salario + (salario * 10) / 100

print('Seu salário passará de R$ {:.2f} reais para R$ {:.2f} reais'.format(salario, aumento))
