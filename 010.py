#10) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no período.

deposito = float(input("insira o valor do deposito: "))
juros = float(input("Insira o valor da taxa de juros: "))
mes = 1
periodo = 12
valor_atual = deposito
while periodo >= 0:
    
    valor_atual = (valor_atual * juros) + valor_atual
    print("no mes", mes,"o saldo da conta é de: %.2f" % valor_atual)
    mes = mes + 1
    periodo = periodo - 1