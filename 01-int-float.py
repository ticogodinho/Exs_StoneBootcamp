#TEMAS: TIPOS NUMERICOS
#DIVERSAO DE CARNAVAL \o/

def exercicio_1():

    from math import log10

    A = int(input("\nDigite um valor para <A>: "))
    B = int(input("\nDigite um valor para <B>: "))

    print(f"\n\n A soma de A e B; {A+B}"
    f"\nA diferenca quando se subtrai B de A; {A-B}"
    f"\nO produto (multiplicacao) entre A e B; {A*B}"
	f"\nO quociente (parte inteira da divisao) quando se divide A por B; {A/B}"
	f"\nO resto da divisao entre A e B; {A%B}"
	f"\nO resultado de log10 de A; {log10(A)}"
	f"\nO resultado de A elevado a B; {A**B}")

def exercicio_2():

    A = int(input("\nDigite a base: "))
    B = int(input("\nDigite a altura: "))

    print((A*B)/2)

def exercicio_3():

    A = int(input("\nDigite os 3 lados do triângulo: "))
    B = int(input())
    C = int(input())

    s = ((A+B+C)/2)

    area = (s*(s-A)*(s-B)*(s-C))**(1/2)

    print(area)

def exercicio_4():

    altura = float(input("\nDigite a altura em metros: "))
    peso = float(input("\nDigite o peso em kilos: "))

    imc = peso/altura**2

    print(f"\nO IMC é: {imc:.2f}")

def exercicio_5():

    digito = input("\nDigite 4 digitos (numéricos): ")

    soma_digitos = int(digito[0]) + int(digito[1]) + int(digito[2]) + int(digito[3])

    print(f"{digito[0]} + {digito[1]} + {digito[2]} + {digito[3]} = {soma_digitos}")

