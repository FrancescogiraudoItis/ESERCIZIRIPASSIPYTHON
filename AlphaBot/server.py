import socket

server_address = ("192.168.1.126", 12345)

BUFFER_SIZE = 4092; #massima dimensione trasmissibile

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)
print("ddgghgffd")
# udp_server_socket.listen(2)
data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto il server
print (f"messaggio ricevuto: {data.decode('utf-8')} da {address}")


udp_server_socket.sendto("Messaggio ricevuto!".encode('utf-8'), address)

udp_server_socket.close()