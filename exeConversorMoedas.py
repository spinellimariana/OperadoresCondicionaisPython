'''
Exercício 10 - Aula 07
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$ 1 = R$3,27
'''
print('***CONVERSOR REAIS PARA DÓLARES***')
print()
reais = float(input('Informe o valor que você possui na sua carteira: '))
print('Com R${} reais você consegue comprar US${:.2f} dólares!'.format(reais, reais/3.27))
