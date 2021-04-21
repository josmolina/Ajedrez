import chess
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




# en main()

hash = HashZobrist()
vN = {0: Hash.tableroHash(tablero)}
TTHash = {Hash.tableroHash(tablero): [0, profundidad, True]}
contador = 1

    def reiniciaHash(vN, TTHash, contador):
        if len(TTHash) >= 500000:
            TTHash = {}
            vN = {}
            contador = 0


def mejorMovimiento3(self,hash, vN, TTHash, contador, profundidad):
    try:
        movida = chess.polyglot.MemoryMappedReader(
            "Perfect2017-LC0.bin").weighted_choice(self.tablero).move
        return movida

    except:
        reiniciaHash(vN, TTHas, contador)
        mejorMovimiento = chess.Move.null()  # Solo pasó el turno al otro jugador
        maxEval = -999999
        alfa = -999999
        beta = 999999
        for movimiento in self.tablero.legal_moves:
            hash = reiniciaHash(tablero, movimiento)
            if hash in TTHash and TTHash[hash][1] >= profundidad and TTHash[hash][2] == False:
                Hash.reiniciarHash(tablero, movimiento)
                if maxEval < TTHash[hash][0]:
                    maxEval = TTHash[hash][0]
                    mejorMovimiento = movimiento
            else:
                tablero.push(movimiento)
                valorEval = -(self.negamax2(-beta, -alfa, profundidad - 1))
                tablero.pop()
                Hash.reiniciarHash(tablero, movimiento)
                TTHash[hash] = [valorEval, profundidad - 1, False]
                vN[contador] = hash
                countador += 1
            alfa = max(valorEval, alfa)
            if alfa >= beta:
                maxEval = valorEval
                mejorMovimiento = movimiento
                break
            if maxEval < valorEval:
                maxEval = valorEval
                mejorMovimiento = movimiento
        return mejorMovimiento


