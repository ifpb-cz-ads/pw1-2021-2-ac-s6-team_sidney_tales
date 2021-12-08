#6) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

#5) Altere o programa abaixo para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

n = int(input("Tabuada de: "))
print("sendo '+' '-' '/' '*' ")
operation = input("insira a operação a qual deseja a tabuada: ")
print("Insira também o valor inicial e o valor final para tabuaada (ex: tabuada de 5 * 15 a 90): ")

start = int(input("Insira o valor inicial: "))
end = int(input("agora insira o valor final: "))
while start <= end:
    if(operation == "+"):
    	    print(n, operation, start, "=", n+start)

    if(operation == "-"):
            print(n, operation, start, "=", n-start)
        
    if(operation == "*"):
            print(n, operation, start, "=", n*start)

    if(operation == "/"):
            print(n, operation, start, "=", n/start)
        
    start = start + 1
    

