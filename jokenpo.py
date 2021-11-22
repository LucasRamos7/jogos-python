import random

def cabecalho():
    print("\n///////////////////////////////")
    print("/// Pedra, papel e tesoura! ///")
    print("///////////////////////////////")

    print ('\nMelhor de cinco!')

def sorteia_pc():
    numero = round(random.randrange(0,3))

    if (numero == 0):
        return 'pedra'
    elif (numero == 1):
        return 'papel'
    elif (numero == 2):
        return 'tesoura'

def pede_aposta():
    print ('\n(1) Pedra  (2) Papel  (3) Tesoura')

    numero = int(input ('Escolha sua jogada! '))

    if (numero == 1):
        return 'pedra'
    elif (numero == 2):
        return 'papel'
    elif (numero == 3):
        return 'tesoura'


def compara_jogadas(aposta_pc, aposta_jogador):
    if (aposta_pc == 'pedra'):
        if (aposta_jogador == 'papel'):
            return 'jogador'
        else:
            return 'pc'
    
    elif (aposta_pc == 'papel'):
        if (aposta_jogador == 'tesoura'):
            return 'jogador'
        else:
            return 'pc'
    elif (aposta_pc == 'tesoura'):
        if (aposta_jogador == 'pedra'):
            return 'jogador'
        else:
            return 'pc'

def jogar():
    cabecalho()

    nome = input ('Insira seu nome: ')

    vitorias_jogador = 0
    vitorias_pc = 0

    while (vitorias_jogador < 3 and vitorias_pc < 3):
        aposta_pc = sorteia_pc()

        aposta_jogador = pede_aposta()

        print (f'\n{aposta_jogador.title()} X {aposta_pc.title()}')
    
        if (aposta_pc == aposta_jogador):
            print ('\nEmpate!')
            print(f'Placar: {nome} {vitorias_jogador} X {vitorias_pc} PC')
        else:
            vencedor = compara_jogadas(aposta_pc, aposta_jogador)

            if (vencedor == 'jogador'):
                print('\nVocê venceu!')
                vitorias_jogador += 1

                print(f'Placar: {nome} {vitorias_jogador} X {vitorias_pc} PC')
            else:
                print('\nVocê perdeu...')
                vitorias_pc += 1

                print(f'Placar: {nome} {vitorias_jogador} X {vitorias_pc} PC')
    
    if (vitorias_jogador == 3):
        print('\nParabéns, você é mais inteligente que o PC!')
    else:
        print('\nVocê foi superado...\n')



if (__name__ == '__main__'):
    jogar()