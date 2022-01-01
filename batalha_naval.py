from classes.tabuleiro import Tabuleiro
from classes.navios import Navio

def cabecalho():
    print("\n/////////////////////")
    print("/// BATALHA NAVAL ///")
    print("/////////////////////")


def jogar():

    cabecalho()
    print('\n\nPosicione os seus navios!\n')

    meu_tabuleiro = Tabuleiro()
    tabuleiro_pc = Tabuleiro()

    meu_tabuleiro.imprimir()

    posicao1 = input('Insira a posição do primeiro extremo do navio: ')
    posicao2 = input('Insira a posição do segundo extremo do navio: ')
    navio = Navio(tamanho=5, extremo1=posicao1, extremo2=posicao2)


if __name__ == '__main__':
    jogar()
