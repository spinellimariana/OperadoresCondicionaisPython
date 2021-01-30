'''
Exercício 14 - Aula 07
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
print('***CONVERSOR DE TEMPERATURAS***')
print()
celcius = float(input('Digite a temperatura em ºC: '))
fahrenheit = (celcius*9/5) + 32
print('Temperatura em Farenheit é de: {:.2f}ºF'.format(fahrenheit))
