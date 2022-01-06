from .navios import Navio


class Tabuleiro():
    def __init__(self):
        self.linhas = [letra for letra in 'ABCDEFGHIJ']
        self.colunas = [numero + 1 for numero in range(10)]
        self.area_navios = [['~' for i in range(10)] for j in range(10)]

    def imprimir(self):
        print(end='    ')
        for letra in self.linhas:
            print(f'{letra}', end='   ')

        print('\n')
        for numero in self.colunas:
            print(f'{numero}', end='')
            if numero != 10:
                print('', end=' ')
            for i in range(10):
                print(f"  {self.area_navios[numero - 1][i]}", end=' ')
            print('\n')

    def posiciona_navio(self, navio: Navio):
        print(navio.posicao)
        for coordenada in navio.posicao:

            letra_coluna = coordenada[:1]
            print(letra_coluna)
            coluna = ord(letra_coluna) - 65
            print(coluna)
            linha = int(coordenada[1:]) - 1
            print(linha)

            self.area_navios[coluna][linha] = 'N'

        self.imprimir()

