class Navio():
    def __init__(self, tamanho, nome):
        self.tamanho = tamanho
        self.nome = nome
        self.posicao = []
        self.golpes = 0
        self.extremos = self.pede_posicoes_navio()
        while not self.aloca_navio(tamanho, self.extremos[0], self.extremos[1]):
            self.extremos = self.pede_posicoes_navio()

        print(f'Navio alocado nas posições {self.posicao[0]}-{self.posicao[-1]}')


    def pede_posicoes_navio(self):
        posicao1 = input(f'Insira a posição do primeiro extremo do {self.nome} ({self.tamanho} espaços): ')
        posicao2 = input(f'Insira a posição do segundo extremo do {self.nome} ({self.tamanho} espaços): ')
        return posicao1, posicao2

    def aloca_navio(self, tamanho, extremo1, extremo2):
        coluna1 = extremo1[:1].upper()
        linha1 = int(extremo1[1:])

        coluna2 = extremo2[:1].upper()
        linha2 = int(extremo2[1:])

        if coluna1 == coluna2 and abs(linha1 - linha2) == tamanho - 1:
            for i in range(min(linha1, linha2), max(linha1, linha2) + 1):
                self.posicao.append(f'{coluna1}{i}')
            return True

        elif linha1 == linha2 and abs(ord(coluna1) - ord(coluna2)) == tamanho - 1:
            for i in range(min(ord(coluna1), ord(coluna2)), max(ord(coluna1), ord(coluna2) + 1)):
                self.posicao.append(f'{chr(i).upper()}{linha1}')
            return True
        else:
            print('Posição inválida!')
            return False


