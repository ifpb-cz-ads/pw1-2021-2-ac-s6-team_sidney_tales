#11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input("insira o valor do deposito: "))
juros = float(input("Insira o valor da taxa de juros: "))
mes = 1
periodo = 12
valor_atual = deposito
new_value = 0
while periodo >= 0:
    
    valor_atual = (valor_atual * juros) + valor_atual
    print("no mes", mes,"o saldo da conta é de: %.2f" % valor_atual)
    new_value = float(input("Insira o valor de um novo deposito: "))
    valor_atual = valor_atual + new_value
    mes = mes + 1
    periodo = periodo - 1