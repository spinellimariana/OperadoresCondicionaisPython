'''
Exercício 11 - Aula 07
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''
print('***TINTA PARA PINTAR A SUA PAREDE***')
print()
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura                                         #Python aceita acentos no nome das variáveis
tinta = área / 2
print('A dimensão da sua parede é de {} x {} e a sua área é de {}m².'.format(largura, altura, área))
print('Será necessário {}L de tinta para pintá-la'.format(tinta))

