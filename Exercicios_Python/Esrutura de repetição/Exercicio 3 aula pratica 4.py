'''
Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. 
Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito, se tiver entre 3 e 12 anos, 
o ingresso custará R$ 15, se tiver mais de 12 anos, custará R$ 30.
escreva um laço que pergunte a idade do usuário e então informe o preço do ingresso.
Encerre o laço com um break quando o usuário sair
Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos,
o total de dinheiro arrecadado e a média de idade das pessoas.
'''

print('Bem Vindo ao cine Patê!')

total_pessoas = 0
dinheiro = 0

while True:
    idade = input('Digite sua idade: ')
    if idade == 'sair':
        break
    idade = int(idade)
    total_pessoas += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total_pessoas

print('Total de pessoas: {}'.format(total_pessoas))
print('Total arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {}'.format(media))
