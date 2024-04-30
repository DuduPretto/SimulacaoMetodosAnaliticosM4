# from enum import Enum
from TipoEvento import TipoEvento
from Fila import Fila

class Evento():
    tipo: TipoEvento
    tempo: float
    fila1: Fila
    fila2: Fila

    def __init__(self, tipo, tempo: float, fila1: Fila, fila2: Fila):
            self.tipo = tipo
            self.tempo = tempo
            self.fila1 = fila1
            self.fila2 = fila2
        
        
    def getTipo(self):
        return self.tipo

    def getTempo(self):
        return self.tempo

    def getFila1(self):
        return self.fila1

    def getFila2(self):
        return self.fila2