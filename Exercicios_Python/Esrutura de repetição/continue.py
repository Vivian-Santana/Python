'''
Escreva um algoritmo que realize um login em um sistema
o usuário deve informar seu nome e senha
'''

print('voltando ao inicio do laço com continue \n')

while True:
    nome =  input('Qual o seu nome? ')
    if(nome != 'lenhadorzinho'):
        continue                # o laço faz voltar ao início até satisfazer a condição.
    senha = input('Qual a sua senha?')
    if(senha == 'UnInTer'):
        break
print('Acesso concedido.')