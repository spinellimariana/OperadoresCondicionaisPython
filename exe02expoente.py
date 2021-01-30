from math import pow
print('***EXPONENCIAÇÃO***')
base = float(input('\nDigite a base: '))
expoente = float(input('Digite o expoente: '))
print('A potência de {:.2f} elevado a {:.2f} é = {:.2f}'.format(base, expoente, pow(base, expoente)))
