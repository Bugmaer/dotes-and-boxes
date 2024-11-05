class Player:
    def __init__(self, number):
        self.numero = number
        self.pontos = 0

    def addPonto(self):
        self.pontos += 1

    def getPontos(self):
        return self.pontos

    def getNumero(self):
        return self.numero
