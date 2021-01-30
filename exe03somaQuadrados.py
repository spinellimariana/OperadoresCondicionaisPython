from math import pow
print('***SOMA DOS QUADRADOS DE DOIS NÚMERO***')
n1 = float(input('\nDigite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
soma = (pow(n1, 2)) + (pow(n2, 2))
print('A soma dos quadrados de {:.2f} + {:.2f} = {:.2f}'.format(n1, n2, soma))

