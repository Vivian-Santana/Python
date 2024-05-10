'''
Escreva um algoritmo que lê um nome e uma idade
Caso o nome digitado seja Vivian, escreva isso na tela
Caso o usuário digite qualquer outro nome, verifique sua identidade.
Se for menor de 18 anos, informe que é menor. Se for maior que 100 anos
informe que esta pessoa possivelmente não existe.
'''
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome == 'Vivian':
    print('Olá {}!' .format(nome))
elif idade < 18:
    print('Você não é a Vivian! E é menor de idade.')
elif idade > 100:
    print('Diferente de você, a Vivian não é imortal!')