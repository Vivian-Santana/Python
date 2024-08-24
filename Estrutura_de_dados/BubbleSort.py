#Bubble sort ordenando array de forma crescente
X = [6, 5, 2, 3, 4, 1]
n = 0
troca = 1
while n <= len(X) and troca == 1:
     troca = 0
     for i in range(0, len(X)-1, 1):
         if X[i] > X[i+1]:
             troca = 1
             aux = X[i]
             X[i] = X[i+1]
             X[i+1] = aux
     n = n + 1
     
print("Vetor ordenado:", X)