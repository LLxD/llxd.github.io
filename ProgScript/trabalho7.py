
def removePontuacao(frase):  # funcao que remove a pontuacao das palavras
    pontuacao = [".",",",":",";","!","?"]
    for sinal in pontuacao:
      frase = frase.replace(sinal, "")
    return(frase)


#verifica se a letra eh igual e determina no final se temos um partial ou um full match
def test_match(key, word, parcial = 0):
    if len(key) == 0: #casos base da recursividade
      if len(word) == 0:
        if parcial == 1:
          return 2
        return 1 #full match
      else:
        return 2 #partial match

    if len(key) > len(word): #não checar caso a chave seja maior que a palavra
      return 0

    if (key[0] == "*") or (key[0] == word[0]): #se letra igual ou wildcard
      if parcial == 1: #verifica se já é um parcial
        return test_match(key[1:], word[1:len(key)+1],1) #se for, retorne apenas o resto da lista até o final do tamanho da chave
      return test_match(key[1:], word[1:]) #se nao for, retorne a lista até o final
    else:
      if len(key) == len(word):
        return 0 #caso sejam de tamanhos iguais porém primeira letra diferentes
      else:
        return test_match(key,word[1:],1) #caso possa ser um parcial





def main():
    completo = ""
    alvo = []

    L = int(input())  # numero de linhas

    for i in range(L):  # receber o texto do usuario, armazenar, separar as palavras e remover as pontuacoes
        texto = str(input())
        removetex = removePontuacao(texto)
        completo = completo + " " + removetex
    completo = completo.lower()

    N = int(input())  # numero de palavras buscadas

    for j in range(N):  # palavras alvo da busca
        texto = str(input())
        alvo.append(texto)

    for k in range(N):  # prints
        partial = 0
        full = 0
        for word in completo.split(): #para cada palavra, chama a função recursiva e verifica o resultado
            result = test_match(alvo[k].lower(), word)
            if result == 1:
              if len(alvo[k]) != len(word):
                # print(alvo[k],word, "PARCIAL")
                partial = partial + 1 
              else:
                # print(alvo[k],word, "FULL")
                full = full +1
            elif result == 2:
                # print(alvo[k],word, "PARCIAL")
                partial = partial + 1
        print("Palavra buscada:", alvo[k])
        print("Ocorrencia:", full)
        print("Palavras similares:", partial)


if __name__ == "__main__":
    main()

# Lucas Lima do Nascimento
# 11721EMT014
