print('DISSECANDO UMA VARIÁVEL')
print()
n = input("Digite alguma coisa: ")
print()
print('O tipo primitivo do valor digitado é:', type(n)) #diz qual é o tipo primitivo da variável
print()
print('Só tem espaços', n.isspace())                    #verifica se só tem espaços
print()
print('É um número?', n.isnumeric())                    #verifica se é um número
print()
print('É alfabético?', n.isalpha())                     #verifica se é alfabético
print()
print('É alphanumérico?', n.isalnum())                  #verifica se é alphanumérico
print()
print('Está em maiúsculas?', n.isupper())               #verifica se está em caixa alta
print()
print('Está em minúsculas?', n.islower())               #verifica se está tudo em letras minúsculas
print()
print('Está captalizado?', n.istitle())                 #verifica se está captalizada

#todos esses comandos retornam valores booleanos - True or False