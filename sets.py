#TEMAS: DICIONÁRIOS E SETS
#DIVERSAO DE CARNAVAL \o/

from operator import itemgetter

def exercicio_1():

    ingles = {
        "João Alves dos Santos", "Maria Magalhães",
        "Antônio da Silva Ferreira", "José Júnior Jarbas",
        "Henrique da Silva Sauro", "Joaquina Ferreira da Silva",
        "Fabiana Aparecida Bianco",	"Marrone Gutierres",
        "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"}

    frances = {
        "João Alves dos Santos", "Antônio da Silva Ferreira",
        "Fernanda Abdala Mohamed", "Abner Mignon Alib", 
        "Alisson Figueiredo", "Henrique da Silva Sauro",
        "Maria Magalhães", "Marrone Gutierres",
        "Joaquina Ferreira da Silva"}
    
    matriculados_tot = ingles|frances
    apenas_ingles = ingles-frances
    apenas_frances = frances-ingles
    matriculados_ambos = ingles&frances
    franc_ou_ingles = apenas_ingles|apenas_frances

    print(
        "\n1.	Quantos estão matriculados na escola, no total?"
        f"\nEstão matriculados na escola {len(matriculados_tot)} pessoas"
        "\n2.	Quantos e quais estão matriculados APENAS em INGLES?"
        f"\nAPENAS em INGLES estão{len(apenas_ingles)} pessoas:\n{apenas_ingles}"
        "\n3.	Quantos e quais estão matriculados APENAS em FRANCES?"
        f"\nAPENAS em FRANCES estão {len(apenas_frances)} pessoas: \n{apenas_frances}"
        "\n4.	Quantos e quais estão matriculados EM AMBOS os cursos?"
        f"\nEM AMBOS os cursos estão {len(matriculados_ambos)} pessoas: \n{matriculados_ambos}"
        "\n5.	Quantos alunos estão matriculados somente em francês ou somente em inglês,"
        " mas não em ambos os cursos?"
        f"\nEstão matriculados somente em francês ou somente em inglês {len(franc_ou_ingles)} pessoas"
)

def exercicio_2():

    estados_siglas = {
        "RR":"Roraima", "AP":"Amapá", "AM":"Amazonas", "PA":"Pará", "AC":"Acre", "RO":"Rondônia", "TO":"Tocantins",
        "MA":"Maranhão", "PI":"Piauí", "CE":"Ceara", "RN":"Rio Grande do Norte", "PB":"Paraiba", "PE":"Pernambuco",
        "AL":"Alagoas", "SE":"Sergipe", "BA":"Bahia", "MT":"Mato Grosso","DF":"Distrito Federal", "GO":"Goiás",
        "MS":"Mato Grosso do Sul", "MG":"Minas Gerais", "ES":"Espírito Santo", "RJ":"Rio de Janeiro", "SP":"São Paulo",
        "PR":"Parana", "SC":"Santa Catarina", "RS":"Rio Grande do sul"}

    sigla = input("Digite a sigla de um estado: ").upper()

    print(f"O nome completo do estado é {estados_siglas.get(sigla)}")

def exercicio_3(): #Printar da maior para a menor, se entendi bem o enunciado...

    dicionario = {"matemática": 81, "física": 83, "química": 87}
    dicionario_novo = {}

    for materia, nota in sorted(dicionario.items(), key=itemgetter(1),reverse=True):
        dicionario_novo[materia] = nota
    print(dicionario_novo)
    
def exercicio_4():

    dicionario = {1: "vermelho", 2: "azul", 3: "marrom"}
    dicionario_novo = {}

    for key, str in dicionario.items():
        dicionario_novo[key] = len(str)
    print(dicionario_novo)

def exercicio_5():

    dicionario = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}
    nota_max = max(dicionario.values())
    nota_min = min(dicionario.values())

    for nome, nota in dicionario.items():
        if nota_max == nota:
            print(f"Nota máxima -> {nome}:{nota_max}")
        if nota_min == nota:
            print(f"Nota mínima -> {nome}:{nota_min}")
