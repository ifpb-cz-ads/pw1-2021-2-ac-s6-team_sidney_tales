# 1) Modifique o programa abaixo para exibir o que se pede:
# a) Exibir os números de 1 a 100.
# b) Exibir os números de 50 a 100. 

a = 1
end = 100
b = 0

#letra a e b
print("Letra A:      Letra B:")
while a<=end:
    if(a < 50):
        print(a)
    if(a >= 50):
        b = a
        print(a,"      ",b)
    a=a+1

