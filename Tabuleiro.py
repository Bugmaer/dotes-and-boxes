
tabuleiro = ["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]

def imprimir_matriz(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))

imprimir_matriz(tabuleiro)
