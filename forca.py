import random


def jogar():
    
    cabecalho()

    tema = escolher_tema()

    palavra_secreta = sorteiar_palavra(tema)

    letras_descobertas = []
    for letra in palavra_secreta:
        letras_descobertas.append('_')

    for index in range(len(letras_descobertas)):
        print (letras_descobertas[index], end = ' ')
    
    print('\n')
    
    chute = input("Chute uma letra! ").lower()
    if (len(chute) > 1):
        input("Chute apenas uma letra! ").lower()

    posicoes_descobertas = []
    posicao = 0
    
    for letra in palavra_secreta:
        if (chute == letra):
            posicoes_descobertas.append(posicao)
        posicao += 1
    

    for index in range(len(posicoes_descobertas)):
        letra_acertada = posicoes_descobertas[index]

        letras_descobertas[letra_acertada] = palavra_secreta[letra_acertada]

    for index in range(len(letras_descobertas)):
        print (letras_descobertas[index], end = ' ')
        
    


    

def cabecalho():
    print("\n///////////////////////////////////////////")
    print("/// Jogo da forca - Adivinhe a palavra! ///")
    print("///////////////////////////////////////////")

def escolher_tema():
    print("\nEscolha o tema: ")
    tema = int(input("(1) Frutas  (2) Esportes (3) Países "))

    while(tema not in [1, 2, 3]):
        print("\nEscolha o tema, de 1 a 3: ")
        tema = int(input("(1) Frutas  (2) Esportes (3) Países "))

    return tema

def sorteiar_palavra(tema):
    if (tema == 1):
        arquivo = open("palavras_forca/frutas.txt", "r")
    elif(tema == 2):
        arquivo = open("palavras_forca/esportes.txt", "r")
    else:
        arquivo = open("palavras_forca/paises.txt", "r")

    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    
    arquivo.close()
    
    palavra_secreta = lista_palavras[round(random.randrange(0, len(lista_palavras)))]

    return palavra_secreta
    

if (__name__ == "__main__"):
    jogar()