import forca
import adivinhacao

def escolher_jogo():

    print('\n/////////////////////////////')
    print('/// Bem vindo ao console! ///')
    print('/////////////////////////////')

    print('\nQual jogo você deseja jogar?')

    jogo = int(input('(1) Adivinhação  (2) Jogo da Forca '))

    while (jogo not in {1, 2}):
        print('\nNúmero de jogo inválido.')
        print('Qual jogo você deseja jogar?')

        jogo = int(input('(1) Adivinhação  (2) Jogo da Forca '))
    
    if (jogo == 1):
        print('Iniciando adivinhação...')

        adivinhacao.jogar()
    elif(jogo == 2):
        print('Iniciando Jogo da Forca...')

        forca.jogar()

if (__name__ == '__main__'):
    escolher_jogo()
        