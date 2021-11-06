import random  


def jogar():
    
    cabecalho()

    numero_secreto = sorteia_numero()
    
    nivel = escolher_dificuldade()

    tentativas = definir_tentativas(nivel)

    print(tentativas)


def cabecalho():
    print("\n//////////////////////////////////")
    print("/// Adivinhe o número secreto! ///")
    print("//////////////////////////////////")

def sorteia_numero():
    numero_secreto = round(random.randrange(0, 101))
    return numero_secreto

def escolher_dificuldade():
    print ("\nEscolha a dificuldade, de 1 a 3")
    dificuldade = int(input("(1) Fácil  (2) Médio  (3) Difícil "))

    while (dificuldade not in [1, 2, 3]):
        print ("\nEscolha a dificuldade, de 1 a 3")
        dificuldade = int(input("(1) Fácil  (2) Médio  (3) Difícil "))
    
    return dificuldade
    #definir_tentativas(dificuldade)
    
def definir_tentativas(dificuldade):
    if (dificuldade == 1):
        numero_de_tentativas = 20

        return numero_de_tentativas
    elif (dificuldade == 2):
        numero_de_tentativas = 10

        return numero_de_tentativas
    elif(dificuldade == 3):
        numero_de_tentativas = 5

        return numero_de_tentativas
    else:
        escolher_dificuldade()


if (__name__ == "__main__"):
    jogar()