#15) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.

menu = " "
x = 1
while menu != "sair":

    print(" -  Escolha um tipo de tabuada digitando a operação desejada  - ")
    print("Menu:")
    print(" - Adição - ")
    print(" - Subtração -")
    print(" - Multiplicação -")
    print(" - Divisão -")
    print(" - ou digite 'sair' para deixar o programa - ")

    menu = input("Escolha uma opção do menu:  ")
    print(menu)
    
    if(menu == "Adição" or menu == "adição" or menu == "adicao" or menu == "ADICAO" or menu == "ADIÇÂO"):
        while x <= 10:
            print(1, " + ", x, "=", 1+x)
            x = x + 1

    if(menu == "Substração" or menu == "subtração" or menu == "subtracao" or menu == "SUBTRACAO" or menu == "SUBTRAÇÃO  "):
        while x <= 10:
            print(1, " - ", x, "=", 1-x)
            x = x + 1
        
    if(menu == "MULTIPLICAÇÃO" or menu == "multiplicacao" or menu == "Multiplicação" or menu == "multiplicação" or menu == "MULTIPLICACAO"):
        while x <= 10:
            print(1, " * ", x, "=", 1*x)
            x = x + 1

    if(menu == "DIVISÃO" or menu == "DIVISAO" or menu == "Divisão" or menu == "divisao" or menu == "divisão"):
        while x <= 10:
            print(1, " / ", x, "=", 1/x)
            x = x + 1

    
        
    