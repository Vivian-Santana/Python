'''
Calcule a média dos números pares de 1 até 100 (1 e 100 inclusos).
Implemente o laço usando for
obs.: A execução repetida de uma sequência de instruções é chamada de iteração (iteration)
'''

soma = 0
qtd = 0
for iterador in range(1,101):
    if (iterador % 2 == 0): # validação se o numero é par
        soma += iterador
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}' .format(media))