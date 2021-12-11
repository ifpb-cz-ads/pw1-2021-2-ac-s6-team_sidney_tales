#8) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de 

#7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
print("ex: first * last = result")
first = int(input("insira o valor do primeiro numero: "))
last = int(input("Insira o valor do numero pelo qual o primeiro será dividido: "))

aux = 0;
result = first
cont = 0
while result - last >= 0:
    result = result - last
    cont = cont + 1
    aux = aux + 1

print("O resultado da divisão de ",first,"por",last,"é igual a: ",cont, "e resto da divisão é: ", result)
