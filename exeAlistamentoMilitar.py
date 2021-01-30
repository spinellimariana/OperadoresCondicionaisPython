'''
Exercício 39 - Aula 12
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
print('***ALISTAMENTO MILITAR***')
nasc = int(input('\nInforme o ano do seu nascimento com 4 dígitos: '))
ano = date.today().year
idade = ano - nasc
print('\nQuem nasceu em {} tem {} anos em {}!'.format(nasc, idade, ano))
if idade < 18:
    falta = 18 - idade
    alistamento = ano + falta
    print('Ainda faltam {} anos para o alistamento!'.format(falta))
    print('\033[1:32mSeu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    passou = idade - 18
    alistamento = ano - passou
    print('Você já deveria ter se alistado há {} anos.'.format(passou))
    print('\033[1:31mSeu alistamento foi em {}'.format(alistamento))
else:
    print('\033[1:33mVocê tem que se alistar IMEDIATAMENTE!')
