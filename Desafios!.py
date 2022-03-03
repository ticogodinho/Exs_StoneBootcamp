#TEMAS: DESAFIOS!!
#DIVERSAO DE CARNAVAL \o/

def desafio_1():

    import random as rd

    restart = "SIM"
    while restart == "SIM":

        num_ale = rd.randint(1,100) # O enunciado indica q o numero deve estar "entre 1 e 100", o q n incluiria
                                # 1 e 100, mas incluí pq não acho que tenha sido essa a intenção (tbm n incluí 
                                # os decimais, pelo msm motivo...)
    
        num_sorte = 0
        while num_sorte < 1 or num_sorte > 100:
            num_sorte = int(input("Digite um numero inteiro entre 1 e 100 (inclusos 1 e 100): "))

        tentativas = 1
        while num_ale != num_sorte:
            if num_ale > num_sorte:
                print("\nO número sorteado é maior que o digitado...")
                num_sorte = int(input("Tente denovo: "))
                
            elif num_ale < num_sorte:
                print("\nO numero sorteado é menor que o digitado...")
                num_sorte = int(input("Tente denovo: "))                
            tentativas = tentativas + 1

        print("\nParabéns! Você acertou o número sorteado :)"
                f"\n Você precisou de {tentativas} tentativas para acertar")
        restart = input("\nDeseja jogar novamente? Se sim digite <SIM>").upper()

    print("\nJogo encerrado, até a próxima!")
    
def desafio_2():

    import random as rd

    restart = "SIM"
    while restart == "SIM":

        dado_1 = rd.randint(1,6)
        dado_2 = rd.randint(1,6)
        soma_dado = dado_1 + dado_2
    
        num_sorte = 0
        while num_sorte < 2 or num_sorte > 12:
            num_sorte = int(input("Digite um numero inteiro entre 2 e 12 (inclusos 2 e 12): "))

        if soma_dado != num_sorte:
            print(f"\nVocê errou. A soma dos dados é {soma_dado}. O valor do primeiro dado é {dado_1}"
                    f" e o do segundo é {dado_2}. ")
        else:
            print("\nParabéns! Você acertou a soma dos dados!"
                    f"\nO valor do primeiro dado é {dado_1} e o do segundo é {dado_2}.")

        restart = input("\nDeseja jogar novamente? Se sim digite <SIM>").upper()

    print("\nJogo encerrado, até a próxima!")

def desafio_3(): # Calcula quantos anagramas a str tem

    str = list(input("Insira uma string: "))

    while " " in str:   # Retira os espaços da string
        str.remove(" ")

    num_carac = len(str)
    permuta_anagramas = 1
    permuta_repeticoes = 1

    for caracteres in range(1, num_carac+1):    # Faz a permutação do numero de caracteres (num_carac!)
        permuta_anagramas = permuta_anagramas*caracteres

    for letra in str:   # Conta e faz a permutação das repetições armazenando em "permuta_repeticoes"
        repeticoes = str.count(letra)

        for letras_repetidas in range(1, repeticoes+1):
            permuta_repeticoes = permuta_repeticoes*letras_repetidas

        if letra in str:    # Retira repetições das letras p/ n contar denovo
            str = str[(str.index(letra)+1):]
            while letra in str:   
                str.remove(letra)

    anagramas = int(permuta_anagramas/permuta_repeticoes)

    print(f" A string digitada tem {anagramas} anagramas")
