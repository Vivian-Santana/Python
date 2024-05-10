'''
Aula 4 tem 4
for usado quando se sabe a quantidade interações que eu quero fazer
assim o número de vezes que o laço vai executar é finito e bem definido.
obs.: A execução repetida de uma sequência de instruções é chamada de iteração (iteration)


omitindo o valor inicial do iterador, por padrão o Python pega a partir de 0.
e omitimos o valor do passo, que por padrão o python pega 1.
'''
for iterador in range(6): # vai imprimir só até o 5 pq a contagem inicia em  0. range sign. intervalo
    print(iterador) # o valor da variável iterador começa em zero pq é o padrão quando não se especifica.
    # iterador é mt chamado de i (incremento) ou cont.
#range é capaz de trabalhar só com uma informação. Quando só uma informação é dada, ela é tratada como sendo o valor final da iteração.

'''
pode-se infromar a à função range 3 valores: 
o 1° valor será sempre o valor inicial da iteração
o 2° será o final
e o 3° e ultimo será o passo
como no exemplo a baixo:⬇️
'''

print('\n Definindo um início para a contagem:')
for i in range(1,6,1): # para i no intervalo de 1 até 5 (pq é 6-1), de um em um
    print(i)

# contagem decremental:
print('\n De trás pra frente:')
for ite in range(10,0,-2): # decremento com passo de duas unidades.
    print(ite)      # como o limite final imposto é 0 ele é excluido do laço.

print ('comparação de for com while mesmo algoritmo:')
x = 1 # valor inicial
while(x < 6): # valor final do iterador
    print(x)
    x= x + 1 # passo do iterador

print('\nfor:')
for iterator in range(1,6,1): # valor inicial -> 1 | valor final do iterador -> 6 | # passo do iterador -> 1
    print(iterator)

print('\nContagem de 10 -> 1.000')
for cont in range(10,1000,1):
    print(cont)