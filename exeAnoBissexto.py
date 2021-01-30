'''
Exercício 32 - Aula 10
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Para ser bissexto:
1) Tem que ser divisivel por 4;
2) Não pode ser divisível por 100
3) Tem que ser divisivel por 400
CONFIRMAR.
'''
print('***É ANO BISSEXTO OU NÃO?***')
from datetime import date #para pegar a data configurada no pc
print('\nDigite 0 para verificar o ano atual!')
ano = int(input('Digite o ano para verificar se é bissexto: '))
if ano == 0:
    ano = date.today().year #atribuir o ano configurado no pc como ano a ser analisado
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} É BISSEXTO!'.format(ano))
else:
    print('\nO ano {} NÃO É BISSEXTO!'.format(ano))
