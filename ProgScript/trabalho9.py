import copy

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


def test_match(key, word):
    if len(key) == 0: #casos base da recursividade
      if len(word) == 0:
        return True #full match
    if key == '':
        return False
    key = key.lower()
    word = word.lower()
    if (key[0] == "*") or (key[0] == word[0]): #se letra igual ou wildcard
      return test_match(key[1:], word[1:]) #se nao for, retorne a lista até o final
    else:
        return False #caso sejam de tamanhos iguais porém primeira letra diferentes


def verificaPalavra(i,j,matriz,palavra): #verifica se existe a palavra alvo em algum dos quatro lugares disponíveis.
    horizontal,vertical,diaginfdir, diagsupdir = [],[],[],[]
    linhasabaixo = len(matriz)-i
    linhasacima = 1+((linhasabaixo-len(matriz))*-1)
    colunasrestantes = len(matriz[0])-j

    #algoritmo para pesquisa dentro das linhas e colunas que estão acima ou abaixo da letra inicial, procurando pela palavra chave.
    if(colunasrestantes >= len(palavra)):
        if(linhasabaixo >= len(palavra) and linhasacima-len(palavra) >= 0):
            for a in range(len(palavra)):
                horizontal.append(matriz[i][a+j])
                vertical.append(matriz[a+i][j])
                diaginfdir.append(matriz[a+i][a+j])
                diagsupdir.append(matriz[i-a][a+j])
        elif(linhasabaixo >= len(palavra)):
            for a in range(len(palavra)):
                horizontal.append(matriz[i][a+j])
                vertical.append(matriz[a+i][j])
                diaginfdir.append(matriz[a+i][a+j])
        elif(linhasacima-len(palavra)>=0):
            for a in range(len(palavra)):
                horizontal.append(matriz[i][a+j])
                diagsupdir.append(matriz[i-a][j+a])
        elif(colunasrestantes>=len(palavra)):
            for a in range(len(palavra)):
                horizontal.append(matriz[i][a+j])
    else:
        if(linhasabaixo >= len(palavra)):
            for a in range(len(palavra)):
                vertical.append(matriz[a+i][j])
        else:
            #em todos os casos, a funcao retorna um array que indica em qual caso
            #há ocorrencia, caso haja.
            return([False,False,False,False])
            
    hor_text = "".join(horizontal)
    ver_text = "".join(vertical)
    diaginf_text = "".join(diaginfdir)
    diagsup_text = "".join(diagsupdir)
    #puxa a funcao recursiva para avaliar a igualdade
    e = test_match(hor_text,palavra)
    r = test_match(ver_text,palavra)
    t = test_match(diaginf_text,palavra)
    y = test_match(diagsup_text,palavra)
    return([e,r,t,y])


def scanMatriz(linhas,colunas,matriz,palavra,matriz_dif): #escaneia a matriz pela letra inicial da palavra
    
    ocorrencias,i, j = 0,0,0
    while i < linhas:
        while j < colunas:
            letrainic = matriz[i][j]
            if (letrainic == palavra[0] or letrainic == "*"): #escanear a matriz pela letra inicial ou por um *
                x = verificaPalavra(i,j,matriz,palavra)
                #x é o vetor de trues e falses para caso haja ocorrencia
                #logo depois vem uma sequencia de ifs para deixar as ocorrencias em maiusculo
                if x[0] == True:
                    for d in range(len(palavra)):
                        matriz_dif[i][j+d] = matriz_dif[i][j+d].upper()
                if x[1] == True:
                    for d in range(len(palavra)):
                        matriz_dif[i+d][j]=matriz_dif[i+d][j].upper()
                if x[2] == True:
                    for d in range(len(palavra)):
                        matriz_dif[i+d][j+d]=matriz_dif[i+d][j+d].upper()
                if x[3] == True:
                    for d in range(len(palavra)):
                        matriz_dif[i-d][j+d]=matriz_dif[i-d][j+d].upper()
                #sum(x) usado para somar os trues (= 1) do vetor, ou seja, calcular o numero de ocorrencias
                ocorrencias = ocorrencias + sum(x)
                j += 1
            else:
                j += 1
        j = 0
        i += 1
    return(ocorrencias,matriz_dif)

def main():
    i = 0
    alvo = []
    
    linhas = int(input())
    colunas = int(input())
    matriz = criaMatriz(linhas,colunas)
    #gerar uma cópia da matriz original
    matriz_dif = copy.deepcopy(matriz)
    N = int(input())  # numero de palavras buscadas

    for j in range(N):  # palavras alvo da busca
        texto = str(input())
        alvo.append(texto)

    #printar
    print("----------------------------------------")
    print("Lista de Palavras")
    print("----------------------------------------")

    for palavra in alvo:
        ocorrencias,matriz_dif = scanMatriz(linhas,colunas,matriz,palavra,matriz_dif)
        print("Palavra:", palavra)
        print("Ocorrencias:", ocorrencias)
        print("----------------------------------------")
    #printar a matriz com letras maiusculas
    while i < linhas:
        linha = " ".join(matriz_dif[i])
        print(linha)
        i += 1


if __name__ == "__main__":
    main()

# Lucas Lima do Nascimento
# 11721EMT014
