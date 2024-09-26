import socket as s #importa il modulo socket e assegna l'alias s
#definisco la porta e l'indirizzo del server
server_address= ('localhost',65432)

#dimensione del buffer per i dati ricevuti
BUFFER_SIZE = 4092 #La dimensione del buffer è di 4092 byte

#crea un socket UDP in modalità client UDP
udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
message="Ciao sono il client".encode()
for i in range(10):
    udp_client_socket.sendto(message, server_address)
    i+1

#Metto in ascolto il client per ricevere la risposta dal server
data, address= udp_client_socket.recvfrom(BUFFER_SIZE)

#stampo il messaggio ricevuto dal server
print(data.decode())
#chiudo il socket
udp_client_socket.close()