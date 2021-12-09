#19) Altere o programa abaixo de forma a imprimir o menor elemento da lista.

lista = [1,7,0,2,4]
minimo = lista[0]
for elemento in lista:
	if elemento < minimo:
    		minimo = elemento
print(minimo)
