import yaml
from Evento import Evento
from TipoEvento import TipoEvento
from Fila import Fila
from Simulador import Simulador


# def main():

#     # Variáveis
#     escalonador = Escalonador()
#     fila = Fila(nroServidores=2, capacidade=5, intervaloChegada=(2, 5), intervaloAtendimento=(3, 5), escalonador=escalonador)

#     count = 100000

#     escalonador.add(2, TipoEvento.CHEGADA)

#     while (count > 0):
#         eventoAtual = escalonador.nextEvent()

#         if eventoAtual.tipo == TipoEvento.CHEGADA:
#             count = fila.chegada(eventoAtual, count)
#         elif eventoAtual.tipo == TipoEvento.SAIDA:
#             count = fila.saida(eventoAtual, count)
#         count -=1

#     print("------------Informações da Fila------------\n")

#     for i in range(fila.capacidade + 1):
#         output_string = f"{i} : {fila.acumuladorTempo[i]} ({fila.acumuladorTempo[i] / fila.tempoTotal * 100:.10f}%)"
#         print(output_string)

#     print("\nTempo total: ", fila.tempoTotal)
#     print("\Total de perdas: ", fila.perdas)





def main():

    with open('dados.yml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        print(data)

    
    listaFilas: list = []
    
    primeiraChegada: int = data['arrivals']["Q1"]
    repeticoes: int = data['rndnumbersPerSeed']

    n1: list = []
    n1.append("q2-0.8")
    n1.append("q3-0.2")

    n2: list = []
    n2.append("q1-0.3")
    n2.append("q1-0.5")
    n2.append("exist-0.2")


    n3: list = []
    n3.append("q3-0.7")
    n3.append("exit-0.3")
    
    listaFilas.append(Fila("q1", 1, 5, [2, 4], [1, 2], n1))
    listaFilas.append(Fila("q2", 2, 5, [0, 0], [4, 8], n2))
    listaFilas.append(Fila("q3", 2, 10, [0, 0], [5, 15], n3))
    
    evento = Evento(TipoEvento.CHEGADA, primeiraChegada, listaFilas[0], None)

    simulador = Simulador(data["seed"][0], listaFilas)

    simulador.executa(evento, repeticoes)

    #prints finais

    for fila in listaFilas:
        print("Infos:")

        print("Fila: (G/G/", fila.nroServidores, "/" ,fila.capacidade, ")")

        
    

if __name__ == "__main__":
    main()