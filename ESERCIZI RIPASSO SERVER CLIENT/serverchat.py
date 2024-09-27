import socket
import threading

def handle_client_connection(connection):
    while True:
        try:
            # Ricevi il messaggio dal client
            message = connection.recv(1024).decode('utf-8')
            if not message:
                print("Il client si è disconnesso.")
                break
            print(f"Client: {message}")
        except:
            print("Errore nella connessione col client.")
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server in ascolto su localhost:65432...")
    
    connection, client_address = server_socket.accept()
    print(f"Connessione stabilita con {client_address}")
    
    # Crea un thread per gestire i messaggi in arrivo dal client
    client_thread = threading.Thread(target=handle_client_connection, args=(connection,))
    client_thread.start()
    
    # Il server invia messaggi al client
    try:
        while True:
            message = input("Server: ")
            connection.sendall(message.encode('utf-8'))
            if message.lower() == "exit":
                break
    finally:
        print("Connessione chiusa.")
        connection.close()

if __name__ == "__main__":
    start_server()
