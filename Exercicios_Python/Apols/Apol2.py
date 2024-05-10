print('a) Calcula e apresenta na tela o somatório de todos os numeros multiplos de 5 até 25')
# soma 5 + 10 + 20 + 15 + 25 = 75
cont = 5
soma = 0
while cont <= 25:
   soma = soma + cont
   cont = cont +5
print(soma)

print('\nB)Soma todos os números de 1 a 25')
cont = 5
soma = 0
while cont <= 25:
   soma = soma + cont
   cont += 1
print(soma)

print('\nC) Printa números de 0 - 100')
x = 0
while(x < 100): # ou (x <= 99)
    print(x)
    x += 1

print('\nD) Printa  5-> 25 pulando 5 numeros (sem while):')
x = 5
print(x)
x += 5
print(x)
x += 5
print(x)
x += 5
print(x)
x += 5
print(x)

print('\nE)Printa  5-> 25 pulando 5 numeros (com while):')
# mesmo q o de cima
x = 5
while x <= 25:
   print(x)
   x += 5 # pula 5 números

print('\nF)Tabuada de soma de 10 até 19 com os numeros: 10,12,14,16 e 18')

for i in range (10,20):
   for j in range (10, 20 , 2):
      print('{} + {} = {}' . format(i, j, i + j))

print('\nG)Tabuada de soma de 10 até 19 com os numeros: 10,12,14,16 e 18 (com while e for)')
# mesmo q o de cima
i = 10
while i < 20:
    j = 10
    while j < 20:
        print('{} + {} = {}'.format(i, j, i + j))
        j += 2
    i += 1

print('\nH)Printa valores de 7 e até o 25, de 3 em 3.')
for i in range (7, 26, 3): # realizar o print na tela de valores numéricos iniciando no 7 e imprimindo até o 25, de 3 em 3.
   print(i)

print('\nI)Printa de 100 até 990 de 10 em 10 (com for)')
for i in range (100, 1000, 10): # imprime de 100 até 990 de 10 em 10 (era pra ser até mil mas como é de 10 em 10 no ultimo passo ele excluiu o 1000).
   print(i)

print('\nJ)Printa de 100 até 990 de 10 em 10 (com while)')
# mesma coisa só que com while
i = 100
while (i <= 999):
   print(i)
   i += 10
#---------------------------------------
print('\nK)Printa de 88 -> 0 de 4 em 4 números com while:')
i = 88
while (i >= 0):
   print(i)
   i -= 4
# mesma coisa q o de cima
print("\nM)Printa de 88 -> 0 de 4 em 4 números com for:")

for i in range(88, -1, -4):
   print(i)

print("\nN) Printa os numeros de 10 -> 100")

x = 10 # variável de controle de loop 
while(x <= 100):
    print(x) # dentro do laço primeiro faz-se o print da variável de controle
    x += 1   # e depois realiza-se o incremento, pois servirá para limitar o número de vezes que o laço é executado.