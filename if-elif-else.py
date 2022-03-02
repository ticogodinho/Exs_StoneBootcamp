#TEMAS: CONDICIONAIS
#DIVERSAO DE CARNAVAL \o/

def exercicio_1():
    num = int(input("\nDigite um número: "))

    if num%2 == 0:
        print("\nO número é par")
    else:
        print("\nO número é impar")

def exercicio_2():

    num1 = int(input("\nDigite um dividendo: "))
    num2 = int(input("\nDigite um divisor: "))

    if num1%num2 == 0:
        print(f"\nO numero {num1} é divisível por {num2}")
    else:
        print(f"\nO numero {num1} não é divisível por {num2}")

def exercicio_3():

# Referencia: "Britadeira":130, "Cortador de grama":106, "Despertador":70, "Cômodo em silêncio":40
    
    valor = int(input("\nDigite o valor medido em decibeis: "))

    if valor > 130:
        print("O ruido é superior ao de uma britadeira")
    elif valor == 130:
        print("O ruido é igual ao de uma britadeira")
    elif valor > 106:
        print("O ruido está entre o emitido por um cortador de grama e uma britadeira")
    elif valor == 106:
        print("O ruido é igual ao de um cortador de grama") 
    elif valor > 70:
        print("O ruido está entre o emitido por um cortador de grama e um despertador")
    elif valor == 70:
        print("O ruido é igual ao de um despertador")
    elif valor > 40:
        print("O ruido está entre o emitido por um cômodo em silêncio e um despertador")
    elif valor == 40:
        print("O ruido é igual ao de um cômodo em silêncio")
    else:
        print("O ruido emitido é inferior ao de um cômodo em silêncio")

def exercicio_4():

    ano = int(input("\nDigite um ano: "))

    if ano%400 == 0:
        print(f"\n {ano} é ano bissexto")
    elif ano%4 == 0 and ano%100 != 0:
        print(f"\n {ano} é ano bissexto")
    else:
        print(f"\n {ano} não é ano bissexto")

def exercicio_5():

    placa = input("\nDigite a placa: ")

    if "-" in placa:
        partes = placa.split("-")     
        if len(partes[0]) == 3 and len(partes[1]) == 4:
            print(partes[0].isalpha() and partes[1].isdigit())
        else:
            print(False)    
    else:
        print(False) 

