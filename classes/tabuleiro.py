class Tabuleiro():
    def __init__(self):
        self.linhas = [letra for letra in 'ABCDEFGHIJ']
        self.colunas = [numero + 1 for numero in range(10)]
        self.area_navios = [['~'] * 10] * 10

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