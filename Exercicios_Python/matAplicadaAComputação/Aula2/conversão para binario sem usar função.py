# conversão para binário sem usar a função bin
numero=int(input('Digite um número inteiro: '))
binario = '' # a variável binario recebe uma string vazia
while numero > 0: # enquanto a variável numero for maior que 0 ...
    binario += str(numero%2)# a variável binario vai sendo atualizada com os restos das divisões. str sign. q os numeros serão covertidos para string
    numero //= 2 # pega a parte inteira da divisão da variável numero.
print(f'O binário correspondente é: {binario[::-1]}') # formatação da saída: o '::' pega tds os valores da variável binario e o '-1' faz o resultado ser impresso de trás para frente