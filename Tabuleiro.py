
tabuleiro = [" ","A","B","C","D"],["1","-","-","-","-"],["","|"," "," "," "],["2","-","-","-","-"],[" ",""," "," "," "],["3","-","-","-","-"],[" ",""," "," "," "],["4","-","-","-","-"]


def imprimir_matriz(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))


imprimir_matriz(tabuleiro)
