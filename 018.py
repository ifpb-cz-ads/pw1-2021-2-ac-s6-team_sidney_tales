print("ex: first * last = result")
first = int(input("insira o valor do primeiro numero: "));
last = int(input("Insira o valor do numero pelo qual o primeiro será dividido: "))

aux = 0;
result = first
cont = 0
while result - last >= 0:
    result = result - last
    cont = cont + 1
    aux = aux + 1

print("O resultado da divisão de ",first,"por",last,"é igual a: ",cont)
print("e resto da divisão é: ", result)
