from Escalonador import Escalonador
from Evento import Evento
from TipoEvento import TipoEvento
from Fila import Fila

def main():

    # Variáveis
    escalonador = Escalonador()
    fila = Fila(nroServidores=1, capacidade=1, intervaloChegada=(1, 2), intervaloAtendimento=(2, 3), escalonador=escalonador)

    count = 100

    escalonador.add(0, TipoEvento.CHEGADA)

    while (count > 0):
        eventoAtual = escalonador.nextEvent()

        if eventoAtual.tipo == TipoEvento.CHEGADA:
            fila.chegada(eventoAtual)
        elif eventoAtual == TipoEvento.SAIDA:
            fila.saida(eventoAtual)

        count -= 1

if __name__ == "__main__":
    main()
