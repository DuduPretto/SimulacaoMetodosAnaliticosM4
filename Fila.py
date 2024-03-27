from Evento import Evento
from Escalonador import Escalonador
from TipoEvento import TipoEvento

class Fila():
    statusAtual: int = 0
    nroServidores: int
    capacidade: int
    intervaloChegada: tuple[int, int]
    intervaloAtendimento: tuple[int, int]
    perdas: int = 0
    acumuladorTempo: list[float] = []
    eventosRealizados: list[Evento] = []
    fila: list[Evento] = []
    escalonador: Escalonador
    tempoTotal: float = 0

    ultimoNumero = 100

    def __init__(self, nroServidores: int, capacidade: int, intervaloChegada: tuple[int, int], intervaloAtendimento: tuple[int, int], escalonador: Escalonador):
        self.nroServidores = nroServidores
        self.capacidade = capacidade
        self.intervaloChegada = intervaloChegada
        self.intervaloAtendimento = intervaloAtendimento
        self.escalonador = escalonador
        for i in range(capacidade + 1):
            self.acumuladorTempo.append(0)


    def nextRandom(self):
        a = 3
        c = 10
        M = 21342141243
        pseudoPuro = ((self.ultimoNumero * a) + c) % M
        self.ultimoNumero = pseudoPuro

        return pseudoPuro / M
    

    def acumulaTempo(self, evento: Evento):
        deltaTempo = evento.tempo - self.tempoTotal
        self.acumuladorTempo[self.statusAtual] += deltaTempo
        self.tempoTotal += deltaTempo


    def chegada(self, evento: Evento, count: int):
        if self.statusAtual < self.capacidade:
            self.acumulaTempo(evento)
            self.statusAtual += 1
            self.fila.append(evento)
            if self.statusAtual <= self.nroServidores:
                self.escalonador.add(((self.intervaloAtendimento[1] - self.intervaloAtendimento[0]) * self.nextRandom() + self.intervaloAtendimento[0]) + self.tempoTotal, TipoEvento.SAIDA)
                count -= 1
        else:
            self.perdas += 1
        self.escalonador.add(((self.intervaloChegada[1] - self.intervaloChegada[0]) * self.nextRandom() + self.intervaloChegada[0]) + self.tempoTotal, TipoEvento.CHEGADA)
        count -= 1
        return count

    def saida(self, evento: Evento, count: int):
        self.acumulaTempo(evento)
        self.statusAtual -= 1
        if self.statusAtual >= self.nroServidores:
            self.escalonador.add(((self.intervaloAtendimento[1] - self.intervaloAtendimento[0]) * self.nextRandom() + self.intervaloAtendimento[0]) + self.tempoTotal, TipoEvento.SAIDA)          
            count -= 1

        return count

