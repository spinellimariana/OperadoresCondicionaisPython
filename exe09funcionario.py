print('***CADASTRO DO FUNCIONÁRIO***')
nome = str(input('\nInforme o nome do funcionário: ')).strip()
cadastro = int(input('Informe o cadastro do funcionário: '))
horasTrab = int(input('Informe as horas trabalhadas: '))
horas = int(input('Informe o valor da hora trabalhada: '))
salario = float(horas * horasTrab)
print('\nO salário de {}, cadastrado(a) no n. {}, é de R$ {:.2f} reais.'.format(nome, cadastro, salario))