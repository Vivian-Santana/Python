idadeAna= 32
idadeBeatriz= 29
print(idadeAna<idadeBeatriz) # falso
print(idadeAna>=idadeBeatriz) # Verdadeiro

# NOT = negação
p=True # p é verdadeiro 
print(not(p)) # ~p é falso
print()

Media=float(input('Média obtida: '))
if Media<70:
    print('Reprovado 😥')
else:
    print('Aprovado!🥳')

print()
# And = E
M= float(input('Média obtida:'))
F=float(input("Total de faltas: "))
if M>= 70 and F<= 20: # and "E" só será true quando as duas preposições foram verdadeiras
    print('Aprovado!🥳')
else:
    print('Reprovado 😥')

print()

Apol1 = float(input('Nota da APOL1: '))
Apol2 = float(input('Nota da APOL2: '))
AP = float(input('Nota da Atividade Prática: '))
PO = float(input('Nota da Prova Objetiva: '))
M = 0.15*Apol1 + 0.15*Apol2 + 0.4*AP + 0.3*PO
print(f'Média: {M:.0f}')
if M < 30:
    print('Reprovado 😥')
elif M >= 30 and M < 67:
    print('Em exame')
elif M >= 67 and M <70:
    print('Aprovado por aredondamento')
else:
    print('Aprovado!🥳')

print()

# Or = ou
rg = input('RG (s/n):')
cpf = input('CPF (s/n):')
if rg == 's' or cpf == 's':
    print('Entrada liberada.')
else:
    print('Entrada não autorizada.')