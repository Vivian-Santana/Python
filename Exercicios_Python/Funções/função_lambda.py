'''
aula 5 tema 5
Funções mais simples, sem nome, chamadas de funções lambda
podem ser escritas em uma só linha de código e dentro do programa principal
'''

res = lambda x: x * x # antes dos ":" é o parâmetro o q vem depois é um calculo de raiz
print(res(3)) # pega o resultado e põe na variável res.

soma = lambda x, y: x + y
print(soma(3, 5))