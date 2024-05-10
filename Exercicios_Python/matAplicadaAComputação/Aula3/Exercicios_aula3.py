from math import pi


print('3. Por meio do Python, faça a representação do número 0,0126551 utilizando', 
                        'a notação científica normalizada com 6 casas decimais.')
a = 0.0126551
print('%.6e' % a) 
# a saída será: 1.265510e-02 o e-02 indica que ele é 10⁻² 

print('\n4. Represente, por meio do Python, o número 432531 utilizando',
             'a notação científica normalizada com 6 casas decimais.')
b = 432531
print('%.6e' % b)

print('\n7. Sabendo que a=5,122132 x 10³ e que b=2,741826 x 10³, calcule a+b por meio do Python.')
a1 = 5.122132e+03
b1 = 2.741826e+03
resultado_7 = a1+b1
print('%.10e' % resultado_7)

print('\n8. Dados os números decimais a=1,758911 x 10² e', 
      'b=4,002234 x 10⁵, por meio do Python, calcule a+b.')
a2 = 1.758911e+02
b2 = 4.002234e+05
resultado_8 = a2+b2
print('%.10e' % resultado_8)

print('\n10. Por meio do Python, calcule a.b onde a=3,445161 x 10³ e b=1,151436 x 10³.')
a3 = 3.445161e+03
b3 = 1.151436e+03
resultado_10 = a3*b3
print('%.10e' % resultado_10)

print('\n12. Considerando os números decimais a=3,445161 x 10³', 
          'e b=1,151436 x 10³, calcule a/b por meio do Python.')
a4 = 3.445161e+03
b4 = 1.151436e+03
resultado_12 = a4/b4
print('%.10e' % resultado_12)

print('\n14. A área de um círculo é dada pela expressão 𝐴 = π𝑟² . Calcule a área referente',
        'a um círculo de raio 12 cm considerando π = 3, 14 e considerando em seguida',
        'π = 3,14159265. Calcule, por meio do Python, o erro absoluto e o erro relativo',
        'entre os dois resultados obtidos.')

# com pi= 3.14 duas casa decimais
raio = 12**2
π = 3.14
area_1 = π * raio
print('\nArea 1 %f'% area_1)

# com π = 3,14159265  com oito casa decimais
area_2 = pi * raio            # o resultado do EA e ER está um pouco diferente da 2 maneira pq aqui estou usando a funçãp pi da biblioteca math.
print('Area 2 %f'% area_2)

# Erro absoluto
print('\nErro absoluto: ', end=" ")
erro_absoluto = abs(area_2 - area_1)
print(erro_absoluto)

# Erro relativo
print('\nErro relativo: ', end=" ")
erro_relativo = abs(erro_absoluto)/abs(area_1)
print(erro_relativo)

print('-------------------------------')
A1=3.14*12**2
A2=3.14159265*12**2
print('Area 1 %f'% A1)
print('Area 2 %f'% A2)
EA=abs(A2-A1)
ER=abs(A2-A1)/abs(A2)
print('\nErro absoluto: ', end=" ")
print(EA)
print('\nErro relativo: ', end=" ")
print(ER)
