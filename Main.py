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

    print("------------Informações da Fila------------\n")

    for i in range(fila.capacidade + 1):
        output_string = f"{i} : {fila.acumuladorTempo[i]} ({fila.acumuladorTempo[i] / fila.tempoTotal * 100:.10f}%)"
        print(output_string)

    print("\nTempo total: ", fila.tempoTotal)
    print("\Total de perdas: ", fila.perdas)

if __name__ == "__main__":
    main()
