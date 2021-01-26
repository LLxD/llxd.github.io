
def criaMatriz(linhas,colunas): #cria uma matriz com os elementos digitados do usuario
    matriz = []
    for i in range(linhas):
        linha = parsing()
        matriz.append(linha)
    return matriz


def parsing(): #quebra a string em uma lista
    string = str(input())
    parsing = string.split()
    return(parsing)


def scanMatriz(linhas,colunas,matriz,C): #escaneia a matriz por numeros 1 e quando encontra um chama a funcao verificaPalito
    contador = 0
    j = 0
    i = 0
    while i < colunas:
        while j < linhas:
            if matriz[j][i] == '1':
                tamanho = verificaPalito(j,i,matriz)
                if tamanho >= C: #compara o tamanho obtido com o limite C
                    contador += 1
                if tamanho+j == len(matriz):
                    j = 0
                    break
                else:
                    j = j + tamanho
                    if j >= len(matriz):
                        j = 0
            else:
                j += 1
        j = 0
        i += 1
    return(contador)

def verificaPalito(j,i,matriz): #verifica os proximos digitos e calcula o tamanho do palito
    tamanhopalito = 1
    k = j + 1
    if k == len(matriz):
        return(tamanhopalito)
    while matriz[k][i] == '1': #olha os proximos valores para calcular o tamanho do palito
        tamanhopalito += 1
        k += 1
        if (k == len(matriz)):
            return(tamanhopalito)
    return(tamanhopalito)


def main():
    P, N, C = parsing()
    matriz = criaMatriz(int(N),int(P))
    resultado = scanMatriz(int(N),int(P),matriz,int(C))
    print(resultado)

if __name__ == "__main__":
    main()

# Lucas Lima do Nascimento
# 11721EMT014
