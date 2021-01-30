print('***DIVISÃO DO MAIOR PARA O MENOR***')
n1 = float(input('\nPrimeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
    divisao = n1 / n2
else:
    divisao = n2 / n1
print('A divisão do maior pelo menor é igual a {:.2f}.'.format(divisao))
