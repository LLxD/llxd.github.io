def ler(num):  # funcao para leitura de dados, adicionando elas numa lista auxiliar
    num = int(num)
    values = []
    temp = 0
    for i in range(num):
        temp = str(input())
        values.append(temp)
    return(values)

def selection_sort_duplo(lista1, lista2 = []): #algoritmo de selection sort rodando em uma ou duas listas simultaneamente
    tam = len(lista1)
    for i in range(tam-1):
        menor_pos = i
        for j in range(i+1, tam):
            if(lista1[j]<lista1[menor_pos]):
                menor_pos = j
        #troca de valores
        lista1[i], lista1[menor_pos] = lista1[menor_pos], lista1[i]
        if lista2 != []: #se existir uma segunda lista, ordene-a baseada na primeira
            lista2[i], lista2[menor_pos] = lista2[menor_pos], lista2[i]

    return lista1,lista2



def criaMatriz(linhas,colunas): #cria uma matriz com os elementos digitados do usuario
    matriz = []
    for i in range(linhas):
        temp = []
        matriz.append(temp)
    return matriz


def ordenaTimes(lista,ntimes): #funcao que recebe a lista e separa os times
    matriz = criaMatriz(ntimes,ntimes-1)
    while lista != []:
        for time in range(ntimes):
            if len(lista) != 0:
                matriz[time].append(lista.pop(len(lista)-1))
    return(matriz)            

def formataMatriz(matriz): #escaneia a matriz e formata
    for linha in range(len(matriz)):
        selection_sort_duplo(matriz[linha])

    return(matriz)


def main():
    T = []
    jogadores = []
    nomes = []
    numeros = []
    N = str(input())
    T = N.split()
    #definimos o numero de jogadores e fazemos a leitura para eles
    jogadores =  ler(T[0])
    #separamos as informacoes de cada jogador
    for jogador in jogadores:
        infos = jogador.split()
        nome = infos[0]
        numero = infos[1]
        nomes.append(nome)
        numeros.append(int(numero))
    #ordenamos as informacoes usando selection sort
    numeros,nomes = selection_sort_duplo(numeros,nomes)

    #ordenamos os times em uma matriz
    matriz = ordenaTimes(nomes,int(T[1]))
    matriz = formataMatriz(matriz)
    #printamos os times
    for linha in range(len(matriz)):
        print("Time",linha+1)
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna])
        print()  


    
if __name__ == "__main__":
    main()

# Lucas Lima do Nascimento
# 11721EMT014
