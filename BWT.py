def BWT(parola):
    
    arrParola = list(parola)
    arrFinale = []
    arrParola.append( "$")

    for i in range(0, len(arrParola)):
        arrFinale.append("".join(arrParola))
        arrParola.insert(len(arrParola), arrParola[0])
        arrParola.pop(0)
        

    print(arrFinale)
    
    n = len(arrFinale)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arrFinale[j] > arrFinale[j + 1]:
                arrFinale[j], arrFinale[j + 1] = arrFinale[j + 1], arrFinale[j]
    
    
    print(arrFinale)
    lunghezza = len(arrParola) -1

    print()
    trasformata = ""
    for i in range(0, len(arrFinale)):
        trasformata = trasformata + arrFinale[i][lunghezza]

    return trasformata  


if __name__ == "__main__":

    parola = input("Dimmi la parola di cui vuoi sapere la trasformata  di Burrows-Wheeler: ")
    BWT(parola)









