print('***VALORES ACEITOS***')
a = int(input('\nDigite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
d = int(input('Digite o valor de D: '))
if b > c and d > a and (c + d) > (a > b) and c > 0 and d > 0 and a % 2 == 0:
    print('\nValores Aceitos!')
else:
    print('\nValores NÃO aceitos!')
