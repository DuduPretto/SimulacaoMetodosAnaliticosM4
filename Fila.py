
import numpy as np
class Fila():
    tempos = []
    statusAtual = 0
    id = ""
    nroServidores = 0
    capacidade = 0
    clientesPerdidos = 0

    intervaloChegada = (0, 0)
    intervaloAtendimento = (0, 0)

    network: list


    def __init__(self, id, nroServidores: int, capacidade: int, intervaloChegada: tuple, intervaloAtendimento: tuple, network: list):
        self.id = id
        self.nroServidores = nroServidores
        self.capacidade = capacidade
        self.intervaloChegada = intervaloChegada
        self.intervaloAtendimento = intervaloAtendimento
        self.network = network
        self.times = [0] * (self.capacidade + 1)
        self.statusAtual = 0
        self.clientesPerdidos = 0

        tempos = [0] * (self.capacidade + 1)

        # tempos = np.zeros(self.capacidade)
        #print(tempos)
    


