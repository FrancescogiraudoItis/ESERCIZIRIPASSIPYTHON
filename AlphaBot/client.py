import socket as s #importa il modulo socket e assegna l'alias s
#definisco la porta e l'indirizzo del server
server_address= ('192.168.1.126',12345)

#dimensione del buffer per i dati ricevuti
BUFFER_SIZE = 4092 #La dimensione del buffer è di 4092 byte

#crea un socket UDP in modalità client UDP
udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
#definisco il messaggio da inviare al server
message="Ciao sono il client".encode()# il messaggio è una stringa codificata in UTF-8
#invio il messaggio al server specificando l'indirizzo e la porta del server
udp_client_socket.sendto(message, server_address)

#Metto in ascolto il client per ricevere la risposta dal server
data, address= udp_client_socket.recvfrom(BUFFER_SIZE)

#stampo il messaggio ricevuto dal server
print(data.decode())
#chiudo il socket
udp_client_socket.close()