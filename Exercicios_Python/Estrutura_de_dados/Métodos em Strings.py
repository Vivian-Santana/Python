'''
Aula 4 tema 5 -> trabalhando com métodos em strings
manipular strings é um assunto muito vasto
uma string é imutável
'''

# s1 = 'algoritmos'
# print(s1)
# s1 [0] = 's' # erro - "TypeError: 'str' object does not support item assignment"

# Mas, com listas, podemos alterá-la
s1 = list('algoritmos')
print(s1) # print separado
print(''.join(s1)) # print agrupado
# agora depois de transformar a string em lista é possível mudar os caracteres dela ou toda ela
s1[1] = 'L'
s1[4] = 'R'
s1[7] = 'M'
print(''.join(s1))

print('\nVerificando caracteres: ')
# verifica se a string inicia com a palavra "lógica".
s2 = 'Lógica de Programação e Algoritmos'
output = s2.startswith('Lógica') # para mostrar a saída do valor boleano eu criei a variável output
print('1 -', output)
# é pra retornar true

# verifica se existe a palavra passada como parâmetro no fim da string
output = s2.endswith('Algoritmos')
print('2 -',output)

# verifica se existe a palavra passada como parâmetro no fim da string
output = s2.endswith('algoritmos')
print('3 -',output)# é pra retornar false

# converte td a string em minúsculo e verifica se a palavra no parâmetro está no fim dela
output = s2.lower().endswith('algoritmos')
print('4 -',output)# é pra retornar true

print('\nConvertendo a string em maiúscula e em mninúscula:')
s3 = 'Análise e desenvolvimento de sistemas'
print(s3.upper()) # converte a string em maiúscula
print(s3.lower()) # converte a string em minúscula

print('\nContando caracteres:')# não tá funcionando
contando_cacteres = s3.count('a') # conta quantos "a" tem na string
print('a -',contando_cacteres)

contando_cacteres = s3.upper().count('a') # se quero saber quantos A maiúsculo tem, converte a string inteira em maiúscula e depois faz a verificação.
print('b -',contando_cacteres) # vai dar 0 pq a string foi convertida pra maiúscula antes da verificação.

contando_palavras = s3.lower().count('sistemas') # contando as palavras inteiras
print('c -', contando_palavras)

print('\nQuebrando strings:')
s4 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
separa_str = s4.split(' ') # função split separa as palavras da string
print(separa_str) # só dá certo com frases inteiras

print('\nSubstituindo strings:')
print(s4)
substituindo_str = s4.replace('mafagafinho', 'gatinho') # substituindo palavras dentro da string
print('1 -', substituindo_str)
substituindo_str = s4.replace('mafagafinho', 'gatinho',1) # substituindo um palavra por outra só uma vez
print('2 -', substituindo_str)

print('\nValidando tipos de dados')
s01 = 'Lógica de Programação e Algoritmos'
s02 = '42'

print(s01.isalnum()) # isalnum só vai retornar true se a string tiver letras, números e acentos. (vai dar false pq essa string s01 tem espaços)
print(s02.isalnum()) # dá true pq só tem números
print()
print(s01.isalpha()) # isalpha só retorna true se a string tiver letras e acentos.(nessa caso dá false)
print(s02.isalpha()) # saída: false
print()

s03 = 'LógicadeProgramaçãoeAlgoritmos'
print(s03.isalnum()) # vai dar true por que a string está sem espaços
