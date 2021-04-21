import pygame as p
import InteligenciaArtificial
import chess
import sys

ALTO = ANCHO = 720
PANELMOVIMIENTOSANCHO = 250
PANELMOVIMIENTOSALTO = ALTO
DIMENSIONES = 8
FPS = 15
IMAGENES = {}
TAMAÑOCASILLA = ALTO // DIMENSIONES


def cargaImagenes():
    IMAGENES["b"]=p.transform.scale(p.image.load("imagenes/b.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["k"] = p.transform.scale(p.image.load("imagenes/k.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["n"] = p.transform.scale(p.image.load("imagenes/n.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["q"] = p.transform.scale(p.image.load("imagenes/q.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["r"] = p.transform.scale(p.image.load("imagenes/r.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["p"] = p.transform.scale(p.image.load("imagenes/p.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["P"] = p.transform.scale(p.image.load("imagenes/bp.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["R"] = p.transform.scale(p.image.load("imagenes/bR.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["Q"] = p.transform.scale(p.image.load("imagenes/bQ.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["N"] = p.transform.scale(p.image.load("imagenes/bN.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["K"] = p.transform.scale(p.image.load("imagenes/bK.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))
    IMAGENES["B"] = p.transform.scale(p.image.load("imagenes/bB.png"), (TAMAÑOCASILLA, TAMAÑOCASILLA))

def main():
    p.init()
    pantalla = p.display.set_mode((ALTO, ANCHO))
    clock = p.time.Clock()
    pantalla.fill(p.Color("white"))
    cargaImagenes()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            creaEstadoJuego(pantalla, chess.Board)
            clock.tick(FPS)
            p.display.flip()



def creaTablero(pantalla):
    colores = [p.Color("white"), p.Color("gray")]
    for fila in range(DIMENSIONES):
        for columna in range(DIMENSIONES):
            color = colores[((fila + columna) % 2)]
            p.draw.rect(pantalla, color, p.Rect(columna * TAMAÑOCASILLA, fila * TAMAÑOCASILLA, TAMAÑOCASILLA,
                                                TAMAÑOCASILLA))


def creaPiezas(pantalla, tablero):
    for f in range(DIMENSIONES):
        for c in range(DIMENSIONES):
            pieza = tablero[f][c]
            if pieza != "--":
                pantalla.blit(IMAGENES[pieza], p.Rect(c*TAMAÑOCASILLA, r*TAMAÑOCASILLA, TAMAÑOCASILLA, TAMAÑOCASILLA))


def creaEstadoJuego(pantalla, tablero):
    creaTablero(pantalla)
    creaPiezas(pantalla, tablero)

main()




def NEGAMAXAB(alfa, beta, profundidad):
    tamañoPV[ply] = ply
    marcador = 0
    mejorMovimiento = 0
    banderaHash = banderaHashAlfa
    if (ply && is_repetition() || fifty >= 100)
        return 0
    nodoPV = beta - alfa > 1

    ##Revisar línea 3129 a 3139, 2666
# Razoring:

def razoring():
    value = eval + 125
    if (value < beta):
        if profundidad == 1:
            valorNuevo = qsearch ()
            return valorNuevo
        valor = += 175
        if valor < beta and profundidad <=3:
            valorNuevo = qsearch()
            if valorNuevo < beta:
                return max(valorNuevo, valor)


def generaHash():
    while(tablero.zobrist)