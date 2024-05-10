'''
Exercicio 5 aula 1
Em uma determinada disciplina, para compor a nota, foram realizadas duas
atividades práticas e uma prova objetiva. A primeira atividade prática corresponde a
20% da nota, a segunda atividade prática corresponde a 30% da nota e a prova
objetiva corresponde a 50% da nota da disciplina. Sabendo que se o estudante
obtiver nota inferior a 30 está reprovado, nota maior ou igual a 30 e menor do que 
70 está em exame final e nota maior ou igual a 70 está aprovado, faça um programa
em Python onde são informadas as notas obtidas nas duas atividades práticas e na
prova objetiva e é informada a nota obtida na disciplina e o resultado (reprovado, em
exame final ou aprovado). Considere a nota da disciplina com uma casa decimal.
''' 

AP1=float(input('Nota da Atividade Prática 1: ')) 
AP2=float(input('Nota da Atividade Prática 2: ')) 
PO=float(input('Nota da Prova Objetiva: ')) 

Nota = 0.2*AP1 + 0.3*AP2 + 0.5*PO 
print(f'Nota da disciplina: {Nota:.1f}')

if Nota<30: 
    print('Reprovado 🥺') 
elif Nota>=30 and Nota<70: 
    print('Em exame 📝') 
else: 
    print('Aprovado! 💯')