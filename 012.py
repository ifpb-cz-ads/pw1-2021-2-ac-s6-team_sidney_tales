#12) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

debito_inicial = float(input("insira o valor da divida: "))
juros = float(input("Insira o valor da taxa de juros mensal: "))
parcela = int(input("Insira o valor das parcelas na qual a divida sera paga: "))
total_parcelas = debito_inicial / parcela
total_pago = (parcela + (parcela * juros)) * total_parcelas
juros_total = total_pago - debito_inicial

print("A divida esta estimada para ser quitada em ",total_parcelas,"meses!")
print("o total pago será de:",total_pago,"R$")
print("o total de juros pago será: ",juros_total,"R$")