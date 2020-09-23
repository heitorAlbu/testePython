

def calcularConsumo(consumoLitroPorKm):
    qtdlitros = 1000/consumoLitroPorKm
    custoFinal = qtdlitros * 2.25
    return (qtdlitros, custoFinal)

def imprimirRelatorio():
    listaCarros = ["fusca", "gol", "uno", "vectra", "peugeout"]
    listaConsumo = [7.0, 10.0, 12.5, 9.0, 14.5]
    for index in range(0, len(listaConsumo)):
        tuplaItem = calcularConsumo(listaConsumo[index])
        print("  " + str(index+1) + " - " + str(listaCarros[index]) + "       "+  str(listaConsumo[index]) + "  -  "+ str(round(tuplaItem[0],1)) +" litros - R$ " + str(round(tuplaItem[1],2)))
