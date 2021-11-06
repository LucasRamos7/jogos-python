import random  


def jogar():
    
    cabecalho()

    numero_secreto = sorteia_numero()
    
    nivel = escolher_dificuldade()

    tentativas = definir_tentativas(nivel)

    print(f"\nVocê tem {tentativas} chances!")   
    
    acertou = adivinhar(tentativas, numero_secreto)
    
    if(acertou):
        print(f"\nParabéns, o número secreto era {numero_secreto}!\n")
    else:
        print(f"\nVocê não conseguiu, o número secreto era {numero_secreto}...\n")


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

def pede_chute():
    chute = int(input("\nAdivinhe o número, de 0 a 100! "))

    return chute

def adivinhar(tentativas, numero_secreto):
    while(tentativas > 0):

        chute = pede_chute()

        acertou = False
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (maior):
            print("\nVocê chutou acima do número secreto!")

            tentativas -= 1
            print(f"Você ainda tem {tentativas} chances!")

        elif(menor):
            print("\nVocê chutou abaixo do número secreto!")

            tentativas -= 1
            print(f"Você ainda tem {tentativas} chances!")

        else:
            acertou = True
            break
    return acertou

if (__name__ == "__main__"):
    jogar()