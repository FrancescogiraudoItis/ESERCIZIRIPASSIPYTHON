import socket
# Definisco l'indirizzo ip e la porta del server
server_address = ("localhost", 65432) #2 dati in tupla, una per l'indirizzo ip, l'altra per la porta

BUFFER_SIZE = 4092; #massima dimensione trasmissibile

#creo un socket UDP per la comunicazione
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# F_INET per IPv4, SOCK_DGRAM per UDP

#collego il socket al server specificato con la funzione bind()
udp_server_socket.bind(server_address)
for i in range(10):
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print (f"messaggio ricevuto: {data.decode('utf-8')} da {address}")
    i+1
#decode la stringa ricevuta in modo UTF-8 per poterla visualizzare

#inviamo un messaggio di conferma al client
udp_server_socket.sendto("Messaggio ricevuto!".encode('utf-8'), address)

#chiudo
udp_server_socket.close()