from Escalonador import Escalonador
from Evento import Evento
from TipoEvento import TipoEvento
from Fila import Fila

def main():

    # Variáveis
    escalonador = Escalonador()
    fila = Fila(nroServidores=2, capacidade=5, intervaloChegada=(2, 5), intervaloAtendimento=(3, 5), escalonador=escalonador)

    count = 100000

    escalonador.add(2, TipoEvento.CHEGADA)
    aux = 0

    while (count > 0):
        eventoAtual = escalonador.nextEvent()

        if eventoAtual.tipo == TipoEvento.CHEGADA:
            count = fila.chegada(eventoAtual, count)
        elif eventoAtual.tipo == TipoEvento.SAIDA:
            count = fila.saida(eventoAtual, count)
        aux += 1

    print("Informações da Fila:")

    for i in range(fila.capacidade + 1):
        print(f"Tempo acumulado no estado {i}: {fila.acumuladorTempo[i]}")
        print(f"Probabilidade de {i} clientes na fila: {fila.acumuladorTempo[i] / fila.tempoTotal}")
        print("---------------------------------")

    print("tempo total: ", fila.tempoTotal)
    print(aux)
    print(fila.perdas)

if __name__ == "__main__":
    main()
