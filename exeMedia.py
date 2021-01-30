'''
Exercício 40 - Aula 12
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''
print('***MÉDIA DOS ALUNOS***')
p1 = float(input('Digite a nota da 1a prova: '))
p2 = float(input('Digite a nota da 2a prova: '))
media = (p1 + p2) / 2
if media < 5.0:
    print('\033[1:31mREPROVADO!')
elif 5.0 <= media <= 6.9:
    print('\033[1:33mEM RECUPERAÇÃO!')
else:
    print('\033[1:32mAPROVADO!')