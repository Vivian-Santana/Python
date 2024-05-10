'''
Exercicio 2 aula 1
É possível resolver problemas relacionados a expressões lógicas por meio do
Python. Considerando as proposições p, q e r onde V(p)=V, V(q)=V e V(r)=F, utilize
o Python para obter o valor lógico das seguintes proposições:
'''
print('a) p+q')
p=True
q=True
r=False
print(p or q)

print('\nb) p+r')
b= True
q=True
r=False
print(p or r)

print('\nc) q.r')
p=True
q=True
r=False
print(q and r)

print('\nd) (q.r)')
p=True
q=True
r=False
print(not(q and r))

print('\ne) q+r')
p=True
q=True
r=False
print(q or r)

print('\nf) p’')
p=True
q=True
r=False
print(not(p))

print('\ng) (p.r)’')
p=True
q=True
r=False
print(not(p and r))