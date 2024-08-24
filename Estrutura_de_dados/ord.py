'''
A função ord() em Python é usada para obter o valor Unicode (ou ASCII) de um caractere.
Essa função recebe um único caractere como argumento e retorna um número inteiro que 
representa o código Unicode do caractere.
ord() aceita apenas um único caractere. Se uma string com mais de um caractere 
for passada, resultará em um erro.
'''

# Obtendo o código Unicode de um caractere
valor_a = ord('a')
valor_A = ord('A')
valor_ç = ord('ç')
valor_emoji = ord('😊')
valor_emoji_2 = ord('😁')

print(valor_a)      # Saída: 97
print(valor_A)      # Saída: 65
print(valor_ç)      # Saída: 231
print(valor_emoji)  # Saída: 128522
print(valor_emoji_2) # Saída: 128513 
print("\n")
'''
Reverso de chr():
A função chr() é o inverso de ord(). Enquanto ord() converte um caractere 
em um número inteiro, chr() converte um número inteiro em um caractere.
'''
print(chr(97))   # Saída: 'a'
print(chr(65))   # Saída: 'A'
print(chr(231))  # Saída: 'ç'
print(chr(128522)) # Saída: '😊'
print(chr(128513)) # Saída: '😁'
