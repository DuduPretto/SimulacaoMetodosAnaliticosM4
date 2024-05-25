from Evento import Evento
from TipoEvento import TipoEvento
from Fila import Fila



class Simulador():
    clientesPerdidos = 0
    tempoTotal = 0.0
    ultimoNumero = 0
    filas = []
    escalonador = []
    nrosUsados = 0

    def __init__(self, semente: int, filas: list):
        self.ultimoNumero = semente
        self.filas = filas

    def escalonar(self, evento: Evento):
        if evento.tipo == TipoEvento.CHEGADA:
            self.chegada(evento.getFila1())
        elif evento.tipo == TipoEvento.SAIDA:
            self.saida(evento.getFila2())
        else:
            self.transferencia(evento.getFila1(), evento.getFila2())

    def adicionaEscalonador(self, min, max, tipo, fila1, fila2):
        tempo = min + (max - min) * self.nextRandom()
        evento = Evento(tipo, tempo + self.tempoTotal, fila1, fila2)
        self.escalonador.append(evento)
        self.nrosUsados += 1

    def executa(self, primeiroEvento: Evento, contagem: int):
        self.escalonador.append(primeiroEvento)

        while(self.nrosUsados < contagem):
            print(self.escalonador[0].getTempo())
            self.escalonador.sort()
            
            proximoEvento = self.escalonador.pop()
            
            for fila in self.filas:
                fila.times[fila.capacidade] = self.calculaTempo(fila, proximoEvento)

            self.tempoTotal = proximoEvento.getTempo()

            self.escalonar(proximoEvento)



    def calculaTempo(self, fila: Fila, evento: Evento):
        tempo = fila.times[fila.capacidade] + (evento.tempo - self.tempoTotal)
        return tempo

    def addFilaDestino(self, id, fila: Fila):
        if id == "saida":
            self.adicionaEscalonador(fila.intervaloAtendimento[0], fila.intervaloAtendimento[1], TipoEvento.SAIDA, fila, None)
        else:
            filaDestino = None
            for f in self.filas:
                if f.id == id:
                    filaDestino = f
                    break
            
            self.adicionaEscalonador(filaDestino.intervaloAtendimento[0], filaDestino.intervaloAtendimento[0], TipoEvento.PASSAGEM, fila, filaDestino)




    def chegada(self, fila: Fila):
        if fila.statusAtual < fila.capacidade:
            fila.statusAtual += 1

            if fila.statusAtual <= fila.nroServidores:
                identificador = self.filaDestino(fila)
                self.addFilaDestino(identificador, fila)

        else:
            fila.clientesPerdidos += 1
        
        self.adicionaEscalonador(fila.intervaloAtendimento[0], fila.intervaloAtendimento[1], TipoEvento.CHEGADA, fila, None)

    def saida(self, fila: Fila):
        fila.statusAtual -= 1
        
        if fila.statusAtual >= fila.nroServidores:
            identificador = self.filaDestino(fila)
            self.addFilaDestino(identificador, fila)
    
    def transferencia(self, primeiraFila: Fila, segundaFila: Fila):
        primeiraFila.statusAtual -= 1
        
        if primeiraFila.statusAtual >= primeiraFila.nroServidores:
            identificador = self.filaDestino(primeiraFila)
            self.addFilaDestino(identificador)

        if segundaFila.statusAtual < segundaFila.capacidade:
            segundaFila.statusAtual += 1

            if segundaFila.statusAtual < segundaFila.nroServidores:
                identificador = self.filaDestino(segundaFila)
                self.addFilaDestino(identificador, segundaFila)
        else:
            segundaFila.perdas += 1
    
                
    def filaDestino(self, fila: Fila):
        soma = 0.0
        prob = self.nextRandom()
        self.nrosUsados += 1
        filaDestino = ""
        
        for n in fila.network:
            split = n.split("-")

            if prob < soma:
                break
            else:
                soma += float(split[1])
                filaDestino = split[0]

        return filaDestino
                
    def nextRandom(self):
        a = 1664525
        c = 1013904223
        M = 4294967296
        pseudoPuro = ((self.ultimoNumero * a) + c) % M
        self.ultimoNumero = pseudoPuro

        return pseudoPuro / M
        