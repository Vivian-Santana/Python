'''
aula prática 4
Realize a sequência de print com for e while:
a) Inteiros de 3 até 12, com 12 incluso
b) Inteiros de 0 até 9, exclindo 9, com passo de 2 (pulando de 2 em 2).
'''

#A
print('for')
for iterador in range(3,13,1): # tbm pode-se omitir o ultimo parâmetro q por default será 1.
    print(iterador)

print('\nwhile')

iterator = 3
while(iterator < 13):
    print(iterator)
    iterator += 1 #incrementando o valor do iterator

print('\n------------------')
# B
print('for')
for i in range (0,9,2):
    print(i)

print('\nwhile') 
x = 0
while(x < 9):
    print(x)
    x += 2