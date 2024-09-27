import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = '10.210.0.40'   #porta del server
port = 8900    #non usare una porta che viene solitamente usata (80, 443)

client_socket.connect((host, port))

data_to_send = "1, 55"
client_socket.send(data_to_send.encode('utf-8'))

message = client_socket.recv(4096)
print(f"Server dice: {message.decode('utf-8')}")

client_socket.close()