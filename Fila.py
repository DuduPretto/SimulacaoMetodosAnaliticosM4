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


    def nextRandom():
        a = 3
        c = 10
        M = 21342141243
        pseudoPuro = ((ultimoNumero * a) + c) % M
        ultimoNumero = pseudoPuro

        return pseudoPuro / M
    

    def acumulaTempo(self, evento: Evento):
        if evento.tipo == TipoEvento.CHEGADA:
            self.acumuladorTempo[self.statusAtual - 1] += evento.tempo - self.tempoTotal
        else:
            self.acumuladorTempo[self.statusAtual + 1] += evento.tempo - self.tempoTotal


    def chegada(self, evento: Evento):
        if self.statusAtual < self.capacidade:
            self.statusAtual += 1
            self.fila.append(evento)
            self.acumulaTempo(evento)
            if self.statusAtual <= self.nroServidores:
                self.escalonador.add(((self.intervaloAtendimento[1] - self.intervaloAtendimento[0]) * self.nextRandom() + self.intervaloAtendimento[0]) + self.tempoTotal, TipoEvento.SAIDA)
        else:
            self.perdas += 1
        self.escalonador.add(((self.intervaloChegada[1] - self.intervaloChegada[0]) * self.nextRandom() + self.intervaloChegada[0]) + self.tempoTotal, TipoEvento.CHEGADA)    

    def saida(self, evento: Evento):
        self.statusAtual -= 1
        self.acumulaTempo(evento)
        if self.statusAtual >= self.nroServidores:
            self.escalonador.add(((self.intervaloAtendimento[1] - self.intervaloAtendimento[0]) * self.nextRandom() + self.intervaloAtendimento[0]) + self.tempoTotal, TipoEvento.SAIDA)          

