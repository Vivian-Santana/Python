'''
Exercicio 2 aula prática 3
Escreva uma algoritmo que leia dois valores numéricos e que pergunte ao usuário qual 
operação ele deseja realizar: adição, subtração, multiplicação ou divisão. 
Exiba na tela o resultado da operação desejada.
'''

print('Calculadora \n')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão \n')
print('Pressione outra tecla para sair \n')

op = input('Qual operação deseja fazer?')
if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

if(op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif(op == '-'):
     res = x - y
     print('Resultado: {} - {} = {}'.format(x, y, res))
elif(op == '*'):
     res = x * y
     print('Resultado: {} * {} = {}'.format(x, y, res))
elif(op == '/'):
      res = x / y
      print('Resultado: {} / {} = {}'.format(x, y, res))
else:
    print('Operação inválida!')

print('Encerrando o programa.')