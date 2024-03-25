# from enum import Enum
from TipoEvento import TipoEvento

class Evento():
    tipo: TipoEvento
    tempo: float


    def __init__(self, tempo: float, tipo: TipoEvento):
        self.tempo = tempo
        self.tipo = tipo