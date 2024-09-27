import socket
import threading

def handle_server_connection(client_socket):
    while True:
        try:
            # Ricevi il messaggio dal server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Il server si è disconnesso.")
                break
            print(f"Server: {message}")
        except:
            print("Errore nella connessione col server.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))
    print("Connesso al server su localhost:65432")

    # Crea un thread per gestire i messaggi in arrivo dal server
    server_thread = threading.Thread(target=handle_server_connection, args=(client_socket,))
    server_thread.start()

    # Il client invia messaggi al server
    try:
        while True:
            message = input("Client: ")
            client_socket.sendall(message.encode('utf-8'))
            if message.lower() == "exit":
                break
    finally:
        print("Connessione chiusa.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
