'''
Escreva um programa que calcule o preço a pagar pelo fornecimento de 
energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: 
R para residências, I para indústrias e C para comércios. (considerando a tapela de custos).
''' 

kwh = float(input('Digite o valor do kwh: '))
tipo = input('Digite o tipo de instalação (R - residencial, C - comercial, I - industrial): ').upper()

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif(tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif(tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Instalação inválida!')

print('Total a pagar: {:.2f}'.format(kwh * preco))
