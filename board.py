class Board:
    def __init__(self):
        self.matriz = self.criarTabuleiro()
        self.quadradosCompletos = [[False, False], [False, False]]  # Controle de quadrados pontuados

    def criarTabuleiro(self):
        return [
            [" ", "A", " ", "B", " ", "C"],
            ["0", "O", " ", "O", " ", "O"],
            [" ", " ", " ", " ", " ", " "],
            ["1", "O", " ", "O", " ", "O"],
            [" ", " ", " ", " ", " ", " "],
            ["2", "O", " ", "O", " ", "O"]
        ]

    def showTabuleiro(self):
        for linha in self.matriz:
            for elemento in linha:
                print(elemento, end=" ")
            print()

    def isQuadradoCompleto(self, i, j):
        # Verifica se o quadrado com bordas está completo
        return (
            self.matriz[i][j + 1] == "-" and   # borda superior
            self.matriz[i + 1][j] == "|" and   # borda esquerda
            self.matriz[i + 1][j + 2] == "|" and # borda direita
            self.matriz[i + 2][j + 1] == "-"   # borda inferior
        )
