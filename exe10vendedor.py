from datetime import date
print('***SALÁRIO DO VENDEDOR***')
nome = str(input('\nInforme o nome do vendedor: ')).strip()
fixo = float(input('Informe o salário fixo de {}: '.format(nome)))
totalVendas = float(input('Informe o valor em dinheiro das vendas efetuadas por {}:'.format(nome)))
salario = fixo + ((totalVendas * 15) / 100)
mes = date.today().month
ano = date.today().year
print('\nO salário de {}, em 0{}/{}, será de R$ {:.2f} reais'.format(nome, mes, ano, salario))
