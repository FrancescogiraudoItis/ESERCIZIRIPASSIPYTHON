#programma server

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #AF_INET indica IPV4

host = '10.210.0.115'
port = 12345    #non usare una porta che viene solitamente usata (80, 443)

server_socket.bind((host, port))  

server_socket.listen(5)     #indica il numero di client massimo che il server è disposto ad accettare


#programma principale

while True:
    client_socket, addr = server_socket.accept()    #la prima è la var. client, la seconda invece è l'address del client
    print(f"Connessione da: {addr}")

    message = client_socket.recv(1024).decode('utf-8')  #manderà un messaggio con grandezza 1024 bit e con codificazione utf-8
    print(f"Messaggio ricevuto dal client: {message}")

    client_socket.send(f"Messaggio ricevuto!".encode('utf-8'))

    client_socket.close()
    print(f"Connessione con: {addr} terminata")  