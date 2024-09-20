import socket

server_address= ('192.168.1.126',6980)
BUFFER_SIZE = 4092

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)

data, address= udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto il server, è bloccante

print(f"Messagio ricevuto: {data.decode} da {address}")