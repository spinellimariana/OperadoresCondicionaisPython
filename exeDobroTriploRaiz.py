'''
Exercício 06 - Aula 07
Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raiz quadrada.
'''
print('***DOBRO, TRIPLO E A RAIZ QUADRADA DE UM NÚMERO***')
print()
n = int(input("Digite um número:"))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('O número digitado é: {};\nSeu dobro é igual a: {};\nSeu triplo é igual a: {};\n'
      'Sua raiz quadrada é igual a: {:.2f}.'.format(n, dobro, triplo, raiz))


