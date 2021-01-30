'''
Exercício 29 - Aula 10
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
print('***RADAR ELETRÔNICO***')
velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    print('O veículo foi MULTADO! Excedeu o limite de 80km/h!')
    multa = (velocidade - 80) * 7
    print('A sua multa custará: R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
