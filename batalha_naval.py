def cabecalho():
    print("\n/////////////////////")
    print("/// BATALHA NAVAL ///")
    print("/////////////////////")


def jogar():

    cabecalho()
    print('\n\nPosicione os seus navios!\n')

    linhas = [letra for letra in 'ABCDEFGHIJ']
    colunas = [numero + 1 for numero in range(10)]

    print(end='    ')
    for letra in linhas:
        print(f'{letra}', end='   ')

    print('\n')
    for numero in colunas:
        print(f'{numero}', end='')
        if numero != 10:
            print('', end=' ')
        for i in range(10):
            print("  ~", end=' ')
        print('\n')

    posicao = input('insira posicao ')
    coluna_inicial = posicao[:1]
    linha_inicial = int(posicao[1:])


if __name__ == '__main__':
    jogar()
