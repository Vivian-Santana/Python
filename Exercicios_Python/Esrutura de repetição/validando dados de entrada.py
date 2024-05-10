'''
aula 04 tema 3
Crie um algoritmo que receba um valor do tipo inteiro via teclado
no entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos;
qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado.
'''

print('Validando a entrada:')

x = int(input('Digite um valor maior do que zero: '))
while(x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...'.format(x))