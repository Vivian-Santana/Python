'''
Crie uma variável de string que receba uma frase qualquer.
Crie uma segunda variável, agora contendo a metade da string digitada. 
Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string.
'''

frase = input('Digite uma frase qualquer: ')
tam = len(frase)

frase2 = frase[:int (tam/2)] # pega a string a partir do inicio até a metade da string armazena na frase2
print(frase2[-2:]) # - no índice significa q eu quero pegar de trás pra frente. e 2 pq eu quero pegar os dois ultimos caracteres.