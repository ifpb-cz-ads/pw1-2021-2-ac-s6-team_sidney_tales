#multiplos do numero qeu vc quiser
x = int(input("insira um numero para saber seus primeiros multiplos: "))
aux = x
while aux <= x+10:
    if(aux % x == 0):
        print(aux)
    aux = aux+1
