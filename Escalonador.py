from Evento import Evento
from TipoEvento import TipoEvento

class Escalonador():
    proxEventos: list[Evento] = []


    def add(self, time: float, tipo: TipoEvento):
        self.proxEventos.append(Evento(time, tipo))
        self.proxEventos.sort(key=lambda x: x.tempo)

    def nextEvent(self):
        return self.proxEventos.pop(0)