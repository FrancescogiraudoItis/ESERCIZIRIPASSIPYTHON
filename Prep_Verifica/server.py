import sqlite3
import socket
import threading


db_path = "./file.db" 
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def leggiRigheFiles(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    # print(f"Nomi delle colonne della tabella {table_name}: {columns}")
    rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    # print("\n")
    return rows

righeFiles = leggiRigheFiles("files")


def leggiRigheFiles(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    # print(f"Nomi delle colonne della tabella {table_name}: {columns}")
    rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    return rows

righeFrammenti = leggiRigheFiles("frammenti")


cursor.close()
conn.close()


#INZIO PARTE LEGATA ALLA CONNESSIONE TCP


HOST = "192.168.1.127"
PORT = 6900

def handle_client(conn, addr):
    print(f"Connessione avvenuta con: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"Messaggio ricevuto: {data}, da: {addr}")
            response = handle_request(data)
            conn.sendall(response.encode("utf-8"))
    except (ConnectionAbortedError, ConnectionResetError):
        print(f"Il cliente {addr}  si è disconnesso - Connessione interrotta")
    except Exception as e:
        print(f"Errorre: {addr} - {e}")
    finally:
        conn.close()
        print(f"Il cliente {addr}  si è disconnesso")

def handle_request(data):
    try:
        if data.startswith("CHECK_FILE:"):
            nome_file = data.split(":")[1]
            for file in righeFiles:
                if file[1] == nome_file:
                    return "OK:SI"
            return "OK:NO"

        elif data.startswith("GET_NUM_FRAGMENTS:"):
            nome_file = data.split(":")[1]
            for file in righeFiles:
                if file[1] == nome_file:
                    return f"OK:{file[2]}"
            return "ERROR:File non trovato"

        elif data.startswith("GET_FRAGMENT_IP:"):
            _, nome_file, num_frammento = data.split(":")
            num_frammento = int(num_frammento)
            for file in righeFiles:
                if file[1] == nome_file:
                    file_id = file[0]
                    for frag in righeFrammenti:
                        if frag[1] == file_id and frag[2] == num_frammento:
                            return f"OK:{frag[3]}"
            return "ERROR:Frammento non trovato"

        elif data.startswith("GET_ALL_FRAGMENT_IPS:"):
            nome_file = data.split(":")[1]
            for file in righeFiles:
                if file[1] == nome_file:
                    file_id = file[0]
                    ips = [frag[3] for frag in righeFrammenti if frag[1] == file_id]
                    if ips:
                        return f"OK:{','.join(ips)}"
                    return "ERROR:Nessun frammento trovato"
        else:
            return "ERROR:Comando non riconosciuto"
    except Exception as e:
        return f"ERROR:{str(e)}"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Il server è in ascolto su {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Connessioni del server: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
