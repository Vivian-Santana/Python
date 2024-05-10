'''
Aula 4
Dados não booleanos também podem ser tratados como True ou false em uma condição, seja esta de uma strutura condicionada ou de um laço.
flasey/False:
número será (int ou float) e string vazia

Truthy/True:
Qualquer outro dado.
qualquer valor que for inteiro, numérico e não for 0 pode ser tratado como true.
'''

nome = '' # valor false
while not nome: # negando o false então vai dar true (mesma coisa que fazer while true)
    nome = input('Digite seu nome: ') # quando digita um nome a string vai ficar false encerrando o laço.
valor = int(input('Digite um número inteiro qualquer: '))
if valor: # posso usar apenas o nome de uma variável numa condição como if e else.
    print('Voce digitou um valor diferente de zero.')
else:
    print('Voce digitou zero.')