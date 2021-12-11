#14) Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:

print("Sejam bem vindos ao mercadinho ADS, boas compras e voltem sempre!")

err = "Produto indisponivel, tente novamente"
produtos = [0.50,1.00,4.00,7.00,err,err,err,err,8.00]
n = int(input("Insira o codigo do produto: "))
preço = 0
cont = 0
while n != 0:
    
    if(produtos[n-1] != err):
        quantidade = int(input("insira a quantidade do produto: "))
        preço = preço + produtos[n-1] * quantidade
        cont = cont + quantidade
    else:
        print(err)
    
    n = int(input("Insira o codigo do produto: "))

print("Muito obrigado pela compra, após a compra de ",cont,"produtos, sua compra esta no valor de :",preço,"R$")
