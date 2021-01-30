'''
Exercício 44 - Aula 12
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
print('='*10,'GERENCIADOR DE PAGAMENTOS','='*10)
preco = float(input('Valor total das compras: R$ '))
print('FORMAS DE PAGAMENTO:'
      '\n[1] à vista dinheiro/cheque;'
      '\n[2] à vista cartão;'
      '\n[3] 2x no cartão;'
      '\n[4] 3x ou mais no cartão')
opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
    total = preco - ((preco * 10)/100)
elif opcao == 2:
    total = preco - ((preco * 5)/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('\nSua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + ((preco * 20)/100)
    parcela = int(input('\nQuantas parcelas? '))
    valorParcela = total / parcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS!'.format(parcela, valorParcela))
else:
    total = preco
    print('Opção inválida!')

print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, total))
