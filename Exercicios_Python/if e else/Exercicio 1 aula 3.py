'''
Exercicio 1 aula 3 
Faça uma lagoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. 
Verifique se os valores formam um triângulo e classifique como:
a) Equilátero (três lados iguiais)
b) Isóceles (dois lados iguais)
c) Escaleno (três lados diferentes)
lembre-se de que, para formar um triângulo, nenhum dos lados pode 
ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois.
'''
A = int(input('Digite o 1° lado do triângulo: '))
B = int(input('Digite o 2° lado do triângulo: '))
C = int(input('Digite o 3° lado do triângulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if(A + B > C) and (A + C > B) and (B + C > A):
        if (A != B) and (A != C) and (B != C):
            print('Triângulo escaleno')
        else:
            if (A == B) and (A == C) and (B == C):
                print('Triângulo equilátero')
            else:
                print('Triângulo isóceles')
    else:
        print('Ao menos um dos valore indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valore sindicados não servem para formar um triângulo.')
