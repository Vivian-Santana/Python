'''
Matemática Aplicada à Computação ao Vivo: Exercícios

1. Sabemos que a lógica matemática está baseada em proposições que podem ser
classificadas como verdadeiras ou falsas e se faz presente em diversos ramos da
ciência com aplicações extremamente importantes em processos dedutivos, na
computação e nos problemas de inteligência artificial. Considerando este contexto, o
que é proposição?

Proposição é um conjunto de palavras ou símbolos que retratam um pensamento de
sentido completo e que pode ser classificado como verdadeiro ou falso.
'''
'''
2. Dadas as proposições simples “p” e “q” onde V(p)=V e V(q)=F, determine o valor
lógico da proposição composta “~p+q”.

~p+q:
~V+F
F+F
F
'''

'''
3. Para a contratação de um professor, uma instituição de ensino quer que este
profissional tenha 36 ou mais meses de experiência em sala de aula e 2 ou mais
publicações nos últimos dois anos. Faça um programa simples em Python onde são
informados por meio do teclado os meses de experiência em sala de aula e o
número de publicações nos últimos dois anos. Após o programa avaliar se os
critérios apresentados pela instituição são atendidos, será apresentada a
mensagem “Atende” ou a mensagem “Não atende”, de acordo com os resultados
obtidos.
'''

print('3)', end= '')
E= float(input('Meses de experiência em sala de aula: '))
P= int(input('Número de publicações nos últimos dois anos: '))
if E >= 36 and P >= 2:
 print('Atende')
else:
 print('Não atende')
