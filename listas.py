#TEMAS: LISTAS
#DIVERSAO DE CARNAVAL \o/

def exercicio_1():

    lista = ["A", "B", "C", "D", "E"]

    print(f"\nElemento {lista[0]} na posição 0"
        f"\nElemento {lista[1]} na posição 1"
        f"\nElemento {lista[2]} na posição 2"
        f"\nElemento {lista[3]} na posição 3"
        f"\nElemento {lista[4]} na posição 4")

def exercicio_2():

    lista = ["A", "B", "C", "D", "E", "1", "2", "3", "4", "5"]

    lista.reverse()

    print(lista)

def exercicio_3():

    lista = [5, 1, 7, 21, 0, 3]

    print(f"O maior elemento é {max(lista)} e está na posição {lista.index(max(lista))}")
    print(f"O maior elemento é {min(lista)} e está na posição {lista.index(min(lista))}")

def exercicio_4():

    temperaturas = []
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    for mes in meses:
        temperaturas.append(float(input(f"Digite a temperatura (°C) media do mes de {mes}: ")))

    media_temp = sum(temperaturas)/len(temperaturas)

    print(f"\n Meses com temperatura acima da media anual de {media_temp}°C:\n")

    for i in range(0, len(meses)):
        if temperaturas[i] > media_temp:
            print (f"{i + 1} - {meses[i]}")

def exercicio_5():

    lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    lst[2][2].append(7000)

    print(lst)

def exercicio_6():

    lst = ["Olá!", "", "meu", "nome", "", "é", "luiz", "", "guilherme", ":)"]

    conta_vazio = lst.count("")

    for i in range(0, conta_vazio):
        lst.remove("")

    print(lst)

def exercicio_7():
#considerando "str" no lugar de "int" na segunda parte do enunciado do exercício
    
    lst = ["1", "7", "99", "15"]
    lista_int = []
    lista_str = []

    for item in lst:
        lista_int.append(int(item))
    lst = lista_int

    print("\n")
    print(lst)

    for item in lista_int:
        lista_str.append(str(item))
    lst = lista_str

    print(lst)
