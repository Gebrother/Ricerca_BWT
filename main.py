if __name__ == "__main__":

    parola = input("Dimmi la parola di cui vuoi sapere la trasformata  di Burrows-Wheeler: ")
    arrParola = list(parola)

    for i in range(len(arrParola) -1, -1, -1 ):
        print(arrParola[i], end="")

