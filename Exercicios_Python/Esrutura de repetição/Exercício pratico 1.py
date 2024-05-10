'''
Exercicio 1 Aula prática 4
mesmo exercicio 2 da aula 3 só que com laço de repetição
diferencial: Repita até que a opção saída seja escolhida.
'''

'''
print('Calculadora \n')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão \n')
print('Pressione outra tecla "s" para sair \n')

op = input('Qual operação deseja fazer?')
if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while(op != 's'):
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

    op = input('Qual operação deseja fazer?')
    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

print('Encerrando o programa...')
'''

# 2 OPÇÃO COM WHILE TRUE

print('Calculadora \n')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão \n')
print('Pressione outra tecla "s" para sair \n')

while True:
    op = input('\nQual operação deseja fazer? ')
    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if(op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
        continue # volta para o começo do laço
    elif(op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif(op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif(op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif(op == 's'):
        break
    else:
        print('Operação inválida!')

print('Encerrando o programa...')
