if __name__ == "__main__":

    parola = input("Dimmi la parola di cui vuoi sapere la trasformata  di Burrows-Wheeler: ")
    arrParola = list(parola)
    arrFinale = []
    arrParola.append( "$")

    for i in range(0, len(arrParola)):
        arrFinale.append("".join(arrParola))
        arrParola.insert(len(arrParola), arrParola[0])
        arrParola.pop(0)
        

    print(arrFinale)
    arrFinale.sort()
    
    print(arrFinale)
    lunghezza = len(arrParola) -1

    print()
    trasformata = ""
    for i in range(0, len(arrFinale)):
        trasformata = trasformata + arrFinale[i][lunghezza]

    print("Trasformata di Burrows-Wheeler Transform: ",  trasformata)
    print()









