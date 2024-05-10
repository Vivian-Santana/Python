# aula 4 tema 2
print('Variável de controle ou iterador:')
x = 1 # Variável de controle ou iterador (vai indo de um em um até o 5).
while(x <= 5): # quando essa condição passa a ser falsa o laço é encerrado.
    print(x)
    x = x + 1 # incremento
print()
x = 0
while(x < 100): # ou (x <= 99)
    print(x)
    x = x + 1

print('\n Exercício com contador:') # variáveis contadoras acrescentam valores constantes em uma variável.
# Escreva um algoritmo que imprima na tela somente valores dentro 
# de um intervalo especificado pelo usuário e que sejam números pares.

inicial = int(input('Qual o valor que você deseja iniciar a contagem? '))
final = int(input('Qual o valor que você deseja encerrar a contagem? '))
x = inicial
while (x <= final):
    if(x % 2 == 0): # verifica se o número é par
        print(x)
    x = x + 1 # contador (iterador)
# obvervar a indentação o if e o incremento está dentro do while o print está dentro só do if.

print('\n Exercício com acumulador:') # variáveis acumuladoras, acumulam totais como um somatório.

'''
Escreva um algoritmo que calcule a sua média de notas em determinada disciplina. 
Assuma que a média final é dada pela média aritmética de cinco notas digitadas.
'''
soma = 0 # variável acumuladora (somatorio de notas)
cont = 1
while(cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma = soma + x 
    cont = cont + 1
    media = soma / 5
print('Média final: {:.2f}' .format(media))

print('\n Operadores especiais de atribuição:') # mesmo codigo q o de cima com duas linhas diferentes

soma_notas = 0 # somatorio de notas
contador = 1
while(contador <= 5):
    x = float(input('Digite a {}ª nota: '.format(contador)))
    soma_notas += x   # equivalente: soma_notas = soma_notas + x
    contador += 1     # equivalente (análogo): contador = contador + 1
    media_final = soma_notas / 5
print('Média final: {}' .format(media_final))
