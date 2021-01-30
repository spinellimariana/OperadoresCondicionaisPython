'''
Exercício 37 - Aula 12
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''
from time import sleep
print('***CONVERSOR DE BASES NUMÉRICAS***')
num = int(input('\nDigite um número inteiro: '))
opcao = int(input('\nEscolha uma das bases para conversão: '
                '\n[1] converter para BINÁRIO;'
                '\n[2] converter para OCTAL;'
                '\n[3] converter para HEXADECIMAL'
                '\nSua opção: '))

if opcao == 1:
    print('\nConvertendo para BINÁRIO...')
    sleep(3)
    print('\n{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) #[2:] para eliminar os dois primeiros caracteres que inficam o tipo de numeração
elif opcao == 2:
    print('\nConvertendo para OCTAL...')
    sleep(3)
    print('\n{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\nConvertendo para HEXADECIMAL...')
    sleep(3)
    print('\n{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\n\033[1;31mOPÇÃO INVÁLIDA!')

