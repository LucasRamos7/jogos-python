import adivinhacao
import forca
import jokenpo


def escolher_jogo():

    print('\n/////////////////////////////')
    print('/// Bem vindo ao console! ///')
    print('/////////////////////////////')

    print('\nQual jogo você deseja jogar?')

    jogo = int(input('(1) Adivinhação  (2) Jogo da Forca  (3) Jo-ken-po '))

    while jogo not in {1, 2, 3}:
        print('\nNúmero de jogo inválido.')
        print('Qual jogo você deseja jogar?')

        jogo = int(input('(1) Adivinhação  (2) Jogo da Forca  (3) Jo-ken-po '))
    
    if jogo == 1:
        print('Iniciando adivinhação...')

        adivinhacao.jogar()
    elif jogo == 2:
        print('Iniciando Jogo da Forca...')

        forca.jogar()
    elif jogo == 3:
        print('Iniciando Jo-Ken-Po...')

        jokenpo.jogar()


if __name__ == '__main__':
    escolher_jogo()
        