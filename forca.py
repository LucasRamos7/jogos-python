import random


def jogar():
    
    cabecalho()

    tema = escolher_tema()

    palavra_secreta = sorteiar_palavra(tema).upper()

    letras_descobertas = []
    for letra in palavra_secreta:
        letras_descobertas.append('_')

    print('Adivinhe!')
    imprime_palavra(letras_descobertas)
    
    erros = 0
    acertou = '_' not in letras_descobertas

    while (erros < 6 and not acertou):

        chute = pegar_chute()

        posicoes_descobertas = verificar_chute(palavra_secreta, chute)

        erros = soma_erros(erros, posicoes_descobertas)      
        
        letras_descobertas = preencher_letras_acertadas(posicoes_descobertas, letras_descobertas, palavra_secreta)

        print('')
        imprime_palavra(letras_descobertas)

        acertou = '_' not in letras_descobertas
        

    mensagem_final(acertou, palavra_secreta)
    


def cabecalho():
    print("\n///////////////////////////////////////////")
    print("/// Jogo da forca - Adivinhe a palavra! ///")
    print("///////////////////////////////////////////")


def escolher_tema():
    print("\nEscolha o tema: ")
    tema = int(input("(1) Frutas  (2) Esportes  (3) Países "))

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
    
def imprime_palavra(letras_descobertas):
    for index in range(len(letras_descobertas)):
        print (letras_descobertas[index], end = ' ')

def pegar_chute():
    print('\n')    

    chute = input("Chute uma letra! ").upper()
    while (len(chute) > 1):
        chute = input("Chute apenas uma letra! ").upper()

    
    return chute

def verificar_chute(palavra_secreta, chute):
    posicoes_descobertas = []
    posicao = 0
    
    for letra in palavra_secreta:
        if (chute == letra):
            posicoes_descobertas.append(posicao)
        posicao += 1

    return posicoes_descobertas

def soma_erros(erros, posicoes_descobertas):
    if (len(posicoes_descobertas) < 1):
        erros += 1
        if (erros < 6):
            print(f'Errou... Você ainda tem {6 - erros} chances!')
    else:
        print ("Boa! Veja como está a palavra:")
    
    return erros

def preencher_letras_acertadas(posicoes_descobertas, letras_descobertas, palavra_secreta):
     for index in range(len(posicoes_descobertas)):
        letra_acertada = posicoes_descobertas[index]

        letras_descobertas[letra_acertada] = palavra_secreta[letra_acertada]
    
     return letras_descobertas

def mensagem_final(acertou, palavra_secreta):
    if (acertou):
        print ('\n\nParabéns, você acertou!\n')
    else:
        print (f'\n\nVocê perdeu... A palavra era {palavra_secreta}!\n')


if (__name__ == "__main__"):
    jogar()