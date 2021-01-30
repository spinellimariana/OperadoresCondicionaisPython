from math import sqrt, pow
print('***CÁLCULANDO BHASKARA***')
a = float(input('\nDigite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = pow(b, 2) - (4 * a * c)

if a == 0 or delta < 0:
    print('Impossível calcular!')
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    print('As raízes da equação são {:.2f} e {:.2f}.'.format(r1, r2))
