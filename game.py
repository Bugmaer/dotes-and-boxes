from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.jogador1 = Player(1)
        self.jogador2 = Player(2)
        self.jogadorAtual = self.jogador1  # Começa com o Jogador 1

    def alternarJogador(self):
        self.jogadorAtual = self.jogador1 if self.jogadorAtual == self.jogador2 else self.jogador2

    def verificarPontuacao(self):
        quadrados = [
            (1, 1), (1, 3),  # Primeira linha de quadrados
            (3, 1), (3, 3)   # Segunda linha de quadrados
        ]

        jogadorPontuou = False
        for index, (i, j) in enumerate(quadrados):
            linhaQuadrado = index // 2
            colunaQuadrado = index % 2

            if not self.board.quadradosCompletos[linhaQuadrado][colunaQuadrado]:
                if self.board.isQuadradoCompleto(i, j):
                    print(f"Quadrado fechado na posição {i}, {j}!")
                    self.jogadorAtual.addPonto()
                    self.board.quadradosCompletos[linhaQuadrado][colunaQuadrado] = True
                    jogadorPontuou = True

        return jogadorPontuou

    def realizarJogada(self):
        ehValido = False
        print(f"Jogador {self.jogadorAtual.getNumero()}'s vez:")

        colunaOrigem = input("Digite a coluna de origem: ").lower()
        linhaOrigem = input("Digite a linha de origem: ")
        colunaFinal = input("Digite a coluna de destino: ").lower()
        linhaFinal = input("Digite a linha de destino: ")

        # Lógica de validação de jogadas
        if (colunaOrigem == "a" and linhaOrigem == "0" and
                colunaFinal == "a" and linhaFinal == "1"):
            self.board.matriz[2][1] = "|"
            ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "0"):
                self.board.matriz[2][1] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "2"):
                self.board.matriz[4][1] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "a" and linhaFinal == "1"):
                self.board.matriz[4][1] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.board.matriz[1][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "a" and linhaFinal == "0"):
                self.board.matriz[1][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "c" and linhaFinal == "0"):
                self.board.matriz[1][4] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.board.matriz[1][4] = "-"
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.board.matriz[2][3] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.board.matriz[2][3] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "c" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.board.matriz[2][5] = "|"
                ehValido = True 

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "0"):
                self.board.matriz[2][5] = "|"
                ehValido = True               
        
        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.board.matriz[3][2] = "-"
                ehValido = True
                
        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "1"):
                self.board.matriz[3][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.board.matriz[3][4] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.board.matriz[3][4] = "-"
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.board.matriz[4][3] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.board.matriz[4][3] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.board.matriz[4][5] = "|"
                ehValido = True 

        if (colunaOrigem.lower() == "c" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.board.matriz[4][5] = "|"
                ehValido = True         

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.board.matriz[3][5] = "-" 
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.board.matriz[3][5] = "-" 
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.board.matriz[5][4] = "-"  
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.board.matriz[5][4] = "-"  
                ehValido = True        

        if (colunaOrigem.lower() == "a" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.board.matriz[5][2] = "-"  
                ehValido = True  

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "a" and linhaFinal == "2"):
                self.board.matriz[5][2] = "-"  
                ehValido = True    

        # Adicionar aqui a lógica para outras jogadas...
        # Exemplo:
        if (colunaOrigem == "b" and linhaOrigem == "0" and
                colunaFinal == "b" and linhaFinal == "1"):
            self.board.matriz[2][3] = "|"
            ehValido = True

        if ehValido:
            print("Jogada Válida!")
            if not self.verificarPontuacao():
                self.alternarJogador()
        else:
            print("Jogada Inválida")

    def showStatus(self):
        self.board.showTabuleiro()
        print(f"Pontos do Jogador 1: {self.jogador1.getPontos()} | Pontos do Jogador 2: {self.jogador2.getPontos()}")

# Instanciando e rodando o jogo
if __name__ == "__main__":
    game = Game()
    
    while True:
        game.showStatus()
        game.realizarJogada()
