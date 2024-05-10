# Expressões lógicas e álgebra booleana
print('not:')
x = True
y = False
print(not x)
print(not y, '\n')

print('and:')
a = True
b = False
print(a and y, '\n')

print('or:')
c = True
d = False
print(c or d)
print('-----------------------------------')

'''
precedência dos operadores:
1. Parênteses;
2. Operadores aritméticos de pontenciação ou raiz;
3. Operadores aritméticos de multiplicação divisão e módulo;
4. Operadores aritméticos de adição e subtração;
5. Operadores relacionais (== | != | > | <);
6. Operadores lógicos not;
7. Operadores lógicos and;
8. Operadores lógicos or;
9. Atribuições
'''

e = 10
f = 1
res = not e > f # e é maior q f mas como eu estou negando com o not o resultado vai ser false 
print(res, '\n')

g = 10
h = 1
i = 5.5
res = (g > h) and (i == h) # verdadeiro e falso em and o resultado é falso
print(res)
