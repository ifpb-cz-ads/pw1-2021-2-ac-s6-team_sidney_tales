number = 1;
cont = 0
soma = 0
while number != 0:
    number = int(input("digite um numero inteiro: "))
    soma = soma + number
    cont = cont + 1

print("A soma de todos os numeros dititados é: ",soma)
print("foram lidos",cont,"numeros")
print("A media dos numeros digitados é: ",soma/cont)
