'''
fução X procedimento
procedimento (procedure) - uma rotina sem retorno
função - uma rotina que retorna um dado a quem a invocou.
'''

# função
def soma3(x = 0, y = 0, z = 0): # cabeçalho da função
    res = x + y + z
    return(res)

# classe principal
retornando = soma3(1,2,3)
print(retornando)

# forma alternativa simplificada
print(soma3(2,2)) # a mesma q a de cima só q td em uma linha só.

# invocando os retornos e colocando em variáveis distintas
retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print('Somatórios: {}, {} e {}.'.format(retornado1, retornado2, retornado3))
# trabalhando com retorno temos mais flexibilidade, posso armazenar o retorno numa variável e manter ela salva pra usar ao longo do código inteiro.