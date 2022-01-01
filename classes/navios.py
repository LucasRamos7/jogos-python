class Navio():
    def __init__(self, tamanho, extremo1, extremo2):
        self.tamanho = tamanho
        self.extremo1 = extremo1
        self.extremo2 = extremo2
        self.posicao = []
        self.golpes = 0
        self.aloca_navio(tamanho, extremo1, extremo2)

    def aloca_navio(self, tamanho, extremo1, extremo2):
        coluna1 = extremo1[:1].upper()
        linha1 = int(extremo1[1:])

        coluna2 = extremo2[:1].upper()
        linha2 = int(extremo2[1:])

        if coluna1 == coluna2 and abs(linha1 - linha2) == tamanho - 1:
            for i in range(min(linha1, linha2), max(linha1, linha2) + 1):
                self.posicao.append(f'{coluna1}{i}')
            print(f'Navio alocado nas posições {self.posicao[0]}-{self.posicao[-1]}')

        elif linha1 == linha2 and abs(ord(coluna1) - ord(coluna2)) == tamanho - 1:
            for i in range(min(ord(coluna1), ord(coluna2)), max(ord(coluna1), ord(coluna2) + 1)):
                self.posicao.append(f'{chr(i).upper()}{linha1}')
            print(f'Navio alocado nas posições {self.posicao[0]}-{self.posicao[-1]}')
        else:
            raise ValueError('Posição inválida')


