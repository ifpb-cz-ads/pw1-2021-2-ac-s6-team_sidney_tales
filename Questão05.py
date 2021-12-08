#5) Altere o programa abaixo para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

n = int(input("Tabuada de: "))
print("sendo '+' '-' '/' '*' ")
operation = input("insira a operação a qual deseja a tabuada: ")
x = 1
while x <= 10:
    if(operation == "+"):
    	    print(n, operation, x, "=", n+x)

    if(operation == "-"):
            print(n, operation, x, "=", n-x)
        
    if(operation == "*"):
            print(n, operation, x, "=", n*x)

    if(operation == "/"):
            print(n, operation, x, "=", n/x)
        
    x = x + 1
    

