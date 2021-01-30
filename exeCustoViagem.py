'''
Exercício 31 - Aula 10
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
print('***CUSTO DA VIAGEM***')
distancia = float(input('Informe a distância em KM: '))
if distancia <= 200:
    preço = 0.50 * distancia
else:
    preço = 0.45 * distancia
#preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 (forma simplificada)
print('O preço da passagem será: R${:.2f} reais'.format(preço))
