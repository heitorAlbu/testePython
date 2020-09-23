import math


def apurarVotacao(listaSist, listaVotos):
    listaResultado = []
    totalVotos = 0;
    for i in range(0, len(listaSist)):
        itemResultado = (listaSist[i] , listaVotos[i])
        totalVotos = totalVotos + listaVotos[i]
        listaResultado.append(itemResultado)

    listaResultado.sort(key=lambda x: x[1], reverse=True)
#i[1] / totalVotos * 100
    for i in listaResultado:
        print(i[0] + "                " + str(i[1]) + "      " + str(round(i[1] / totalVotos * 100,2)) + " %")

def abrirVotacao():
    listaSist = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    listaVotos = [0, 0, 0, 0, 0, 0,]
    escolha = -1
    print("Votação : ")
    for index in range(0 , len(listaSist)):
        print(str(index + 1)+ " )" + listaSist[index])
    print("7 ) Apurar Votação")
    while(escolha != 0):
        print("digite o código do Sistema  : ")
        escolha = int(input())

        if escolha == 0:
            print("fim da Votação")
        else:
            if escolha -1 == 0:
                print("Windows Server...")
                listaVotos[0] = listaVotos[0] + 1
            elif escolha -1 == 1:
                print("Unix...")
                listaVotos[1] = listaVotos[1] + 1
            elif escolha - 1 == 2:
                print("Linux...")
                listaVotos[2] = listaVotos[2] + 1
            elif escolha - 1 == 3:
                print("Netware...")
                listaVotos[3] = listaVotos[3] + 1
            elif escolha - 1 == 4:
                print("Mac OS...")
                listaVotos[4] = listaVotos[4] + 1
            elif escolha - 1 == 5:
                print("Outro...")
                listaVotos[5] = listaVotos[5] + 1
            elif escolha - 1 == 6:
                apurarVotacao(listaSist, listaVotos)
            else:
                print("Votação inválida...")