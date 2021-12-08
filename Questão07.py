#7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
print("ex: first * last = result")
first = int(input("insira o valor do primeiro numero:"))
last = int(input("Insira o valor do numero pelo qual o primeiro será multiplicado: "))

aux = 1
result = first
while aux < last:
    result = result + first

    aux = aux + 1

print("O resultado da multiplicação de ",first,"por",last,"é igual a: ",result)
