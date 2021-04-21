import random
import sys

class HashZobrist(object):
    lista = [[]for i in range(64)]

    def __int__(self):
        self.lista = lista = [{} for i in range(64)]
        self.hash = 0
        for piezas in self. lista:
            self.valoresPiezas(piezas)


    def valoresPiezas(self, piezas):
        pieces["K"] = random.randint(0, sys.maxint)
        pieces["Q"] = random.randint(0, sys.maxint)
        pieces["R"] = random.randint(0, sys.maxint)
        pieces["B"] = random.randint(0, sys.maxint)
        pieces["P"] = random.randint(0, sys.maxint)
        pieces["N"] = random.randint(0, sys.maxint)
        pieces["k"] = random.randint(0, sys.maxint)
        pieces["q"] = random.randint(0, sys.maxint)
        pieces["r"] = random.randint(0, sys.maxint)
        pieces["b"] = random.randint(0, sys.maxint)
        pieces["p"] = random.randint(0, sys.maxint)
        pieces["n"] = random.randint(0, sys.maxint)

    def tableroHash(self, tablero):
        for i in range(64):
            hash = tablero.piece_at(i)
            if hash != None:
                self.hash = self.hash ^ (self.lista[i][hash.symbol()])
        return self.hash

    def hash(self, tablero, movimiento):
        if tablero.piece_at(move.to_square) != None:
            self.hash = self.hash ^ (self.lista[movimiento.to_square][tablero.piece_at(movimiento.to_square).symbol()])
        pieza = tablero.piece_at(movimiento.from_square).symbol()
        self.hash = self.hash ^ (self.lista[movimiento.to_square][pieza])
        self.hash = self.hash ^ (self.lista[movimiento.from_square][pieza])
        return self.hash