'''
Condicionais de multipla escolha

Escreva um algoritmo em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. 
Deverá ser apresentado na tela um menu com opções: 1 para maçã, 2 para laranja e 3 para banana
Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. 
O algoritmo deve colacular o preço total a pagar do produto escolhido e mostra-lo na tela
Considere que uma maçã custa R$ 2,30 uma laranja custa R$ 3,60 e uma banana custa R$ 1,85

elif é uma simplificação de else if
'''

print('Escolha o que deseja comprar: ')
print('1 - maçã')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual a sua escolha? '))
quantidade = int(input('Quantas unidades? '))
if(produto == 1):
    total = quantidade * 2.3
    print('Você comprou {} maçãs.\n Total a pagar: {}' .format(quantidade, total))
elif(produto == 2):
        total = quantidade * 3.6
        print('Você comprou {} laranjas.\n Total a pagar: {}' .format(quantidade, total))
elif(produto == 3):
     total = quantidade * 1.85
     print('Você comprou {} bananas.\n Total a pagar: {}' .format(quantidade, total))
else:
    print('Esse produto não existe!')