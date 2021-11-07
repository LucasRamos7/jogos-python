import random


def jogar():
    
    cabecalho()

    tema = escolher_tema()

    palavra_secreta = sorteiar_palavra(tema)

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