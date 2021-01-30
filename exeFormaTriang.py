'''
Exercício 35 - Aula 10
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-='*20)
print('***FORMA OU NÃO UM TRIÂNGULO!***')
print('-='*20)
ladoA = float(input('\nDigite o comprimento do lado A: '))
ladoB = float(input('Digite o comprimento do lado B: '))
ladoC = float(input('Digite o comprimento do lado C: '))

if ladoA >= ladoB + ladoC or ladoB >= ladoA + ladoC or ladoC >= ladoA + ladoB:
    print('\nOs valores informados NÃO FORMAM TRIÂNGULO!')
else:
    print('\nOs valores informados formarão um triângulo!')
