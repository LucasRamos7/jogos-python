from classes_batalha_naval.tabuleiro import Tabuleiro
from classes_batalha_naval.navios import Navio


def cabecalho():
    print("\n/////////////////////")
    print("/// BATALHA NAVAL ///")
    print("/////////////////////")


def jogar():

    cabecalho()
    print('\n\nPosicione os seus navios!\n')

    tabuleiro_jogador = Tabuleiro()
    tabuleiro_pc = Tabuleiro()

    tabuleiro_jogador.imprimir()

    porta_avioes_jogador = Navio(tamanho=5, nome='Porta-Aviões')
    tanque1_jogador = Navio(tamanho=4, nome='Tanque 1')
    tanque2_jogador = Navio(tamanho=4, nome='Tanque 2')
    destroyer1_jogador = Navio(tamanho=3, nome='Destroyer 1')
    destroyer2_jogador = Navio(tamanho=3, nome='Destroyer 2')
    destroyer3_jogador = Navio(tamanho=3, nome='Destroyer 3')
    submarino1_jogador = Navio(tamanho=2, nome='Submarino 1')
    submarino2_jogador = Navio(tamanho=2, nome='Submarino 2')
    submarino3_jogador = Navio(tamanho=2, nome='Submarino 3')
    submarino4_jogador = Navio(tamanho=2, nome='Submarino 4')


if __name__ == '__main__':
    jogar()
