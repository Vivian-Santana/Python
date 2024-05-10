# Atividade prática com o prof Renan Portela Jorge - aula prática 4

print('🍕 Bem vindo a Pizzaria Mama Mia!') # identificação pessoal

print('------------------------Cardápio------------------------')
print('Codigo | descrição | pizza média (M)  |pizza grande (G)|')
print('    21 | Napolitana|      R$ 20,00    |       26,00    |')
print('    22 | Margherita|      R$ 20,00    |       26,00    |')
print('    23 | Calabresa |      R$ 25,00    |       32,50    |')
print('    24 | Toscana   |      R$ 30,00    |       39,00    |')
print('    25 | Portuguesa|      R$ 30,00    |       39,00    |')
print('--------------------------------------------------------')

acumulador = 0

while True:
    tamanho = input('Digite o tamanho da pizza desejada (M | G): ').upper()
    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida! escolha um tamanho válido.')
        continue # se o usuário digitar algo inválido volta para o início do while.
    codigo = input('Digite o código da pizza desejada (21 | 22 | 23 | 24 | 25): ')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print('Opção inválida! escolha um código válido.')
        continue

    if codigo == '21' and tamanho == 'M':
        print('Pizza napolitana - média')
        acumulador += 20 # o iterador q guarda valores, pega o valor q foi guardado na variável e soma com 20
    
    elif codigo == '21' and tamanho == 'G':
        print('Pizza napolitana - grande')
        acumulador += 26

    elif codigo == '22' and tamanho == 'M':
        print('Pizza Margherita - média')
        acumulador += 20

    elif codigo == '22' and tamanho == 'G':
        print('Pizza Margherita - grande')
        acumulador += 26

    elif codigo == '23' and tamanho == 'M':
        print('Pizza Calabresa - média')
        acumulador += 25

    elif codigo == '23' and tamanho == 'G':
        print('Pizza Calabresa - grande')
        acumulador += 32.50
    
    elif codigo == '24' and tamanho == 'M':
        print('Pizza Toscana - média')
        acumulador += 30

    elif codigo == '24' and tamanho == 'G':
        print('Pizza Toscana - grande')
        acumulador += 39

    elif codigo == '25' and tamanho == 'M':
        print('Pizza Portuguesa - média')
        acumulador += 30

    elif codigo == '25' and tamanho == 'G':
        print('Pizza Portuguesa - grande')
        acumulador += 39

    pedir_mais = input('\nDeseja algo mais? (S | N)').upper()
    if pedir_mais == 'S':
        print()
        continue
    else:
        print('\ntotal:{:.2f}'.format(acumulador))
        print('\nSeu pedido está sendo preparado 🍕, você será avisado quando estiver a caminho 🏍️.','\nAgradecemos pela preferência 💕, volte sempre!')
        break
