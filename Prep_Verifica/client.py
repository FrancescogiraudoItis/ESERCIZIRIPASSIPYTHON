import socket

HOST = "192.168.1.127" 
PORT = 6900    

def send_request(request):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(request.encode("utf-8"))
            response = s.recv(1024).decode("utf-8")
            return response
    except Exception as e:
        return f"ERROR:{str(e)}"

if __name__ == "__main__":
    while True:
        print("\nOpzioni:")
        print("1. Controlla se un file è presente")
        print("2. Ottieni il numero di frammenti di un file")
        print("3. Ottieni l'IP di un frammento specifico")
        print("4. Ottieni tutti gli IP di un file")
        print("5. Esci")

        choice = input("Seleziona un'opzione: ")
        if choice == "1":
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"CHECK_FILE:{nome_file}")
        elif choice == "2":
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"GET_NUM_FRAGMENTS:{nome_file}")
        elif choice == "3":
            nome_file = input("Inserisci il nome del file: ")
            num_frammento = input("Inserisci il numero del frammento: ")
            response = send_request(f"GET_FRAGMENT_IP:{nome_file}:{num_frammento}")
        elif choice == "4":
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"GET_ALL_FRAGMENT_IPS:{nome_file}")
        elif choice == "5":
            break
        else:
            print("Opzione non valida")
            continue

        print("Risposta dal server:", response)
