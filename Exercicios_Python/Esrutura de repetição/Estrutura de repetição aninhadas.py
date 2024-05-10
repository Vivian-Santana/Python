'''
Aula 4 tema 5
Calcule a tabuada de todos os números de 1 até 10, e para cada número vamos 
calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.
obs.: A execução repetida de uma sequência de instruções é chamada de iteração (iteration).
'''

tabuada = 1
while tabuada <= 10: # para cada iteração desse primeiro laço acontecem 10 vezes a iteração no laço interno.
    print('Tabuada do {}'.format(tabuada))
    x = 1 # x é o número q se comporta como iterador do laço
    while x <= 10:
        print('{} x {} = {}'.format(tabuada, x, tabuada * x))
        x += 1
    tabuada += 1

# mesmo exercicio só que agora com for
print('\n*** tabuada do 1 ao 10 com for ***')
for tabuada in range(1,11,1):
    print('Tabuada do {}'.format(tabuada))
    for iter in range(1,11,1):
        print('{} x {} = {}'.format(tabuada, iter, tabuada * iter))

# mesmo exercicio com while e for
print('\n*** tabuada do 1 ao 10 com while e for ***')

tabuada3 = 1
while tabuada3 <= 10:
    print('Tabuada do {}'.format(tabuada3))
    for i in range(1,11,1):
        print('{} x {} = {}'.format(tabuada3, i, tabuada3 * i))
    tabuada3 += 1