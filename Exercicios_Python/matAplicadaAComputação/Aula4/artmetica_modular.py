'''
A aritmética modular considera o resto de uma divisão
Se considerarmos, por exemplo, os números 0, 1, 2, 3, 4, temos um
conjunto com 5 elementos e, neste caso, as operações são mod 5.
Por exemplo,
(3+4) mod 5 = 7 mod 5 = 2
Neste caso, fazemos a soma 3+4 que corresponde a 7. Em seguida,
dividimos 7 por 5, cujo resultado é 1 com resto igual a 2. Portanto, 3+4 módulo 5
é igual a 2.
Este conjunto com 5 elementos pode, por exemplo, estar associado às
vogais “a”, “e”, “i”, “o” e “u”. Se estamos considerando a terceira vogal “i” e
avançamos 4 vogais, vamos passar por “o”, “u”, retornamos à vogal “a” e
chegaremos na vogal “e”. A aritmética modular relacionada às vogais é mod 5,
pois há 5 vogais e a aritmética modular relacionada às letras do alfabeto é mod
26, pois há 26 letras no alfabeto. Em Python, o resto da divisão indicado pelo
operador %.
'''
a = 15 % 12
print(a)

print()

b = (3+4) % 5
print(b)

# 14. Obtenha a soma 7+8 módulo 12.
m = (7+8) % 12
print('\n14) {}'.format(m))
