if __name__ == "__main__":

    parola = input("Dimmi la parola di cui vuoi sapere la trasformata  di Burrows-Wheeler: ")
    arrParola = list(parola)
    copiaArr = arrParola
    arrFinale = []
    copiaArr.append( "$")

    for i in range(0, len(copiaArr)):
        arrFinale.append("".join(copiaArr))
        copiaArr.insert(len(copiaArr), copiaArr[0])
        copiaArr.pop(0)
        

    print(arrFinale)
    arrFinale.sort()
    
    print(arrFinale)
    lunghezza = len(copiaArr) -1

    print()
    trasformata = ""
    for i in range(0, len(arrFinale)):
        trasformata = trasformata + arrFinale[i][lunghezza]

    print("Trasformata di Burrows-Wheeler Transform: ",  trasformata)
    print()









