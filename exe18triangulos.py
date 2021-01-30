print('***FORMANDO TRIÂNGULOS***')
a = float(input('\nDigite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

#COLOCANDO OS LADOS EM ORDEM DECRESCENTE:
if a > b:
    if b > c:
        ladoA = a
        ladoB = b
        ladoC = c
    elif c > b:
        ladoA = a
        ladoB = c
        ladoC = b
    else:
        ladoA = c
        ladoB = a
        ladoC = b
elif b > c:
    if a > c:
        ladoA = b
        ladoB = a
        ladoC = c
    elif c > a:
        ladoA = b
        ladoB = c
        ladoC = a
else:
    ladoA = c
    ladoB = b
    ladoC = a
print('Ordem descrescente dos lados: {}, {}, {}.'.format(ladoA, ladoB, ladoC))

#COMPARANDO PARA VER QUAL TIPO DE TRIÂNGULO FORMA:

if ladoA >= ladoB + ladoC:
    print('\033[1:31mNÃO FORMA TRIÂNGULO!')
elif (ladoA*ladoA) == (ladoB * ladoB) + (ladoC * ladoC):
    print('TRIÂNGULO RETÂNGULO!')
elif (ladoA*ladoA) > (ladoB * ladoB) + (ladoC * ladoC):
    print('TRIÂNGULO OBTUSÂNGULO!')
elif (ladoA*ladoA) < (ladoB * ladoB) + (ladoC * ladoC):
    print('TRIÂNGULO ACUTÂNGULO!')

if ladoA == ladoB == ladoC:
    print("TRIÂNGULO EQUILÁTERO!")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('TRIÂNGULO ISÓSCELES!')