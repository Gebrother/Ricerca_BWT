import socket

from BWT import BWT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind(("127.0.0.1", 5000))
    server.listen()

    print("Server in ascolto...")

    conn, addr = server.accept()

    with conn:

        print("Client connesso:", addr)

        messaggio = conn.recv(1024).decode()

        print("Parola ricevuta:", messaggio)

        risultato = BWT(messaggio)

        print("Trasformata BWT:", risultato)

        conn.sendall(risultato.encode())



